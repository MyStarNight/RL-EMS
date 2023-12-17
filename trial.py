import numpy as np
import matplotlib.pyplot as plt

gamma = 0.9

# 模拟电价：参考论文-FEDERATED REINFORCEMENT LEARNING FOR ENERGY MANAGEMENT OF MULTIPLE SMART HOMES
price_dict = {
    1: 6,
    2: 6,
    3: 6,
    4: 6,
    5: 6,
    6: 6,
    7: 6,
    8: 6,
    9: 12,
    10: 14,
    11: 14,
    12: 11,
    13: 14,
    14: 14,
    15: 14,
    16: 14,
    17: 12,
    18: 12,
    19: 12,
    20: 12,
    21: 12,
    22: 12,
    23: 6,
    24: 6,
    25: 6
}


usage_duration = {
    1: 2,
    2: 2,
    3: 2,
    4: 2,
    5: 2,
    6: 2,
    7: 2,
    8: 2,
    9: 4,
    10: 5,
    11: 5,
    12: 3,
    13: 5,
    14: 5,
    15: 5,
    16: 5,
    17: 4,
    18: 3,
    19: 3,
    20: 3,
    21: 3,
    22: 3,
    23: 2,
    24: 2,
    25: 2
}

# 设置当前一天的初始电量为50
energy_start_state = 10

# 设置1h最多可以冲10电量
max_charging_per_hour = 10

# 设置额定负载为5
energy_consumed_per_hour = 5

# 设置EMS的三个Actions
all_possible_actions = ('C', 'D', 'U')

def money_saved_calculaton(actions, price_dict, usage_duration, charge_rate=5):
    money_without_ess = 0
    for hour in range(1, 25):
        money_without_ess += price_dict[hour] * usage_duration[hour]

    money_with_ess = 0
    for hour in range(1, 25):
        if actions[hour-1] == "charge":
            money_with_ess += price_dict[hour] * (usage_duration[hour] + charge_rate)
        elif actions[hour-1] == "discharge":
            continue
        elif actions[hour-1] == "use_grid":
            money_with_ess += price_dict[hour] * usage_duration[hour]

    return  money_without_ess, money_with_ess, money_without_ess-money_with_ess

def action_choice(energy_storaged, energy_used):
    '''
    本函数用来选择ess的action
    :param energy_storaged: 当前电池的容量
    :param energy_used: 电池需要使用的容量
    :return: action
    '''
    if energy_storaged >= energy_used:
        action = np.random.choice(all_possible_actions)
    else:
        action = np.random.choice(('C', 'U'))
    return action

def reward_calculation(s, energy_used, action, price):
    '''
    本函数用来计算ess的reward
    :param energy_charged:充电功率
    :param energy_used: 需要使用的电量
    :param actions: 选择的action
    :param price: 当前电价
    :return: reward
    '''
    if action == 'C':
        reward = -price * (max_charging_per_hour + energy_used)
    elif action == 'D':
        if energy_used <= s[0]:
            reward = 0
        else:
            reward = -1000
    elif action == 'U':
        reward = -price * energy_used
    return reward

def state_change(s, energy_used:int, hour:int, action:str):
    energy_stored = s[0]
    if action == 'C':
        energy_stored = min(energy_stored + max_charging_per_hour, 100)
    elif action == 'D':
        energy_stored = energy_stored - energy_used

    next_state = (energy_stored, price_dict[hour+1])
    return next_state

def energy_management_system(price_dict:dict, policy):

    s = (energy_start_state, price_dict[1])
    a = policy[1]

    # keep track of all states and rewards encountered
    states = [s]
    actions = [a]
    rewards = [0]

    for hour, price in price_dict.items():
        r = reward_calculation(s=s,
                               energy_used=energy_consumed_per_hour,
                               action=a,
                               price=price)
        rewards.append(r)


        if hour != len(price_dict):
            s = state_change(s=s,
                             energy_used=energy_consumed_per_hour,
                             hour=hour,
                             action=a
                             )
            states.append(s)

            a = policy[hour+1]
            actions.append(a)

    return states, actions, rewards

def max_dict(d):
  # returns the argmax (key) and max (value) from a dictionary
  # put this into a function since we are using it so often

  # find max val
  max_val = max(d.values())

  # find keys corresponding to max val
  max_keys = [key for key, val in d.items() if val == max_val]

  ### slow version
  # max_keys = []
  # for key, val in d.items():
  #   if val == max_val:
  #     max_keys.append(key)

  return np.random.choice(max_keys), max_val

if __name__ == '__main__':
    policy = {}
    for hour in price_dict.keys():
            policy[hour] = np.random.choice(all_possible_actions)

    Q = {}
    sample_counts = {}

    for hour in price_dict.keys():
        Q[hour] = {}
        sample_counts[hour] = {}
        for a in all_possible_actions:
            Q[hour][a] = 0
            sample_counts[hour][a] = 0

    # repeat until convergence
    deltas = []
    for it in range(10000):
        if it % 1000 == 0:
            print(it)

        biggest_change = 0
        states, actions, rewards = energy_management_system(price_dict, policy)

        states_actions = list(zip(states, actions))

        T = len(price_dict)
        G = 0
        for t in range(T-2, -1, -1):
            s = states[t]
            a = actions[t]

            G = rewards[t+1] + gamma * G

            # if (s, a) not in states_actions[:t]:
            if True:
                old_q = Q[t+1][a]
                sample_counts[t+1][a] += 1
                lr = 1 / sample_counts[t+1][a]
                Q[t+1][a] = old_q + lr * (G - old_q)

                policy[t+1] = max_dict(Q[t+1])[0]

                biggest_change = max(biggest_change, np.abs(old_q - Q[t+1][a]))


        deltas.append(biggest_change)

    plt.plot(deltas)
    plt.show()

    print(f"final policy:{policy}")

    V = {}
    for t, Qs in Q.items():
        V[t] = max_dict(Q[t])[1]

    print(f"final values:{V}")




