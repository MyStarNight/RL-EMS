import environment
import numpy as np
import pandas as pd


def processing_data(price_dict, consumption_dict):
    for hour, price in price_dict.items():
        price_dict[hour] = round(price)

    for hour, consumption in consumption_dict.items():
        electricity_usage = consumption / 60
        consumption_dict[hour] = round(electricity_usage)

    return price_dict, consumption_dict

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

    return money_without_ess, money_with_ess, money_without_ess-money_with_ess

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

def q_learning_train(price_dict:dict, consumption_dict:dict, battery_dict: dict, num_episode=10000, exploration_rate=0.1, learning_rate=0.1):
    # 获取一天24h的价格以及使用时间
    grid_price, grid_consumption = processing_data(price_dict, consumption_dict)
    price_set = sorted(list(set(grid_price.values())))

    # EMS，启动！
    ems = environment.EMS_MDP(grid_price=grid_price,
                              battery_capacity=battery_dict["capacity"],
                              max_charge_rate=battery_dict["max_charge_rate"],
                              max_discharge_rate=battery_dict["max_discharge_rate"])

    # 得到所有状态state
    all_states = [(energy, price) for energy in range(int(ems.battery_capacity+1)) for price in price_set]

    # 设定q_values和采样数的字典
    q_values, sample_counts = {}, {}
    for state in all_states:
        q_values[state], sample_counts[state] = {}, {}
        for action in environment.all_possible_actions:
            q_values[state][action], sample_counts[state][action] = 0, 0

    # 进行q learning训练
    for episode in range(1, num_episode + 1):
        # 重置EMS，回到初始状态
        state = ems.reset(energy_start=np.random.randint(0, 61))
        total_reward = 0

        states = [state]
        actions = []
        rewards = []
        while True:
            # 设定当前状态下的充放电功率
            ems.charge_discharge(charge_rate=ems.max_charge_rate, discharge_rate=grid_consumption[ems.time_hour])

            # 选择动作
            action = environment.choose_action(ems.state[0], ems.charge_rate, ems.discharge_rate, ems.battery_capacity, exploration_rate=exploration_rate, q_values=q_values, state=state)

            # 样本计数
            sample_counts[state][action] = sample_counts[state][action] + 1
            # learning_rate = 1 / sample_counts[state][action]

            # 执行动作
            next_state, reward = ems.step(action)

            # 更新q值
            q_values[state][action] = q_values[state][action] + learning_rate * (
                    reward + ems.gamma * max_dict(q_values[next_state])[1] - q_values[state][action]
            )

            total_reward += reward
            state = next_state
            states.append(state)
            actions.append(action)
            rewards.append(reward)

            if len(actions) == len(grid_price) - 1:
                break

        if episode % 1000 == 0 or episode == num_episode - 1:
            print(f"Episode {episode}, Total Reward: {total_reward}")

    q_values_result = pd.DataFrame(q_values).T
    sample_counts_result = pd.DataFrame(sample_counts).T

    print("")
    for action, state in zip(actions, states[:-1]):
        print(f"this state: {state}, this action: {action}")

    money_without_ess, money_with_ess, money_saved = money_saved_calculaton(actions, grid_price,grid_consumption,charge_rate=ems.charge_rate)
    print(f"\nMoney without Energy Management: {money_without_ess}$Eu")
    print(f"Money with Energy Management: {money_with_ess}Eu")
    print(f"EMS have saved {money_saved}Eu")

    return states, actions, rewards, q_values_result, sample_counts_result

