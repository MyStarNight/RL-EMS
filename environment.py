import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from tqdm import tqdm
import function

all_possible_actions = ["charge", "discharge", "use_grid"]

class EMS_MDP():
    def __init__(self,
                 grid_price: dict,
                 battery_capacity=20,
                 max_charge_rate=5,
                 max_discharge_rate=5,
                 gamma=0.9,
                 ):
        self.battery_capacity = battery_capacity
        self.max_charge_rate = max_charge_rate
        self.max_discharge_rate = max_discharge_rate
        self.charge_rate = 0
        self.discharge_rate =0
        self.gamma = gamma
        self.grid_price = grid_price
        self.state = None # [energy, price]
        self.time_hour = 0

    def reset(self, energy_start=10):
        # 重置状态
        self.time_hour = 1
        self.state = (energy_start, self.grid_price[self.time_hour])
        return self.state

    def charge_discharge(self, charge_rate, discharge_rate):
        # 执行动作并获取奖励和下一个状态
        # self.charge_rate = self.max_charge_rate  # 充电功率可以调整
        # self.discharge_rate = np.random.randint(0, self.max_discharge_rate+1)  # 放电功率可以调整
        # self.discharge_rate = self.max_discharge_rate
        # self.discharge_rate = np.random.randint(3, self.max_discharge_rate+1) # 假设额定负载为3
        self.charge_rate = charge_rate
        self.discharge_rate = discharge_rate
        return self.charge_rate, self.discharge_rate

    def step(self, action):
        self.time_hour = self.time_hour + 1
        if action == "charge":
            next_energy = min(self.state[0] + self.charge_rate, self.battery_capacity)
            next_price = self.grid_price[self.time_hour]
            self.state = (next_energy, next_price)
        elif action == "discharge":
            next_energy = max(self.state[0] - self.discharge_rate, 0)
            next_price = self.grid_price[self.time_hour]
            self.state = (next_energy, next_price)
        elif action == "use_grid":
            next_energy = self.state[0]
            next_price = self.grid_price[self.time_hour]
            self.state = (next_energy, next_price)

        reward = action_cost(action, self.charge_rate, self.discharge_rate, self.grid_price[self.time_hour-1])

        return self.state, reward

def action_cost(action, charge_rate, discharge_rate, price):
    # 奖励是根据相对来说使用原价省了多少钱
    if action == "charge":
        return -charge_rate * price
    elif action == "discharge":
        return discharge_rate * price
    elif action == "use_grid":
        return 0

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

def choose_action(energy_state, charge_rate, discharge_rate, capacity:int, exploration_rate, q_values, state):
    if energy_state + charge_rate <= capacity and energy_state - discharge_rate >=0:
        # 一切正常
        if np.random.rand() < exploration_rate:
            action = np.random.choice(all_possible_actions)
            return action
        else:
            action = max_dict(q_values[state])[0]
            return action
    elif energy_state - discharge_rate <=0:
        # 电池电量不够使用，只能充电和使用市电
        if np.random.rand() < exploration_rate:
            action = np.random.choice([all_possible_actions[0], all_possible_actions[2]])
            return action
        else:
            action = max_dict({"charge": q_values[state]["charge"], "use_grid": q_values[state]["use_grid"]})[0]
            return action
    elif energy_state + charge_rate >= capacity:
        # 电池电量充足，放电和使用市电
        if np.random.rand() < exploration_rate:
            action = np.random.choice([all_possible_actions[1], all_possible_actions[2]])
            return action
        else:
            action = max_dict({"discharge": q_values[state]["discharge"], "use_grid": q_values[state]["use_grid"]})[0]
            return action


if __name__ == '__main__':
    # 获取一天24h的价格
    grid_price, grid_consumption = function.price_dict, function.consumption_dict
    grid_price, grid_consumption = function.processing_data(grid_price, grid_consumption)
    price_set = sorted(list(set(grid_price.values())))

    # EMS，启动！
    ems = EMS_MDP(grid_price=grid_price, battery_capacity=60, max_charge_rate=6, max_discharge_rate=3)

    # 得到所有状态state
    all_states = []
    for energy in range(int(ems.battery_capacity)+1):
        for price in price_set:
            state = (energy, price)
            all_states.append(state)

    # 设定q_values和采样数的字典
    q_values, sample_counts = {}, {}
    for state in all_states:
        q_values[state], sample_counts[state] = {}, {}
        for action in all_possible_actions:
            q_values[state][action], sample_counts[state][action] = 0, 0
    # df = pd.DataFrame(q_values).T

    # 开始进行q learning的训练
    num_episode = 10000     # 迭代次数
    exploration_rate = 0.5  # 贪心epsilon
    learning_rate = 0.1     # learning rate
    # for episode in tqdm(range(num_episode)):
    for episode in range(1, num_episode+1):
        # 重置EMS，回到初始状态
        state = ems.reset(energy_start=np.random.randint(0, 61))
        total_reward = 0

        states = [state]
        actions = []
        rewards = []
        while True:
            # 设定当前状态下的充放电功率
            # ems.charge_discharge(charge_rate=ems.max_charge_rate, discharge_rate=np.random.randint(3, ems.max_discharge_rate+1))
            ems.charge_discharge(charge_rate=ems.max_charge_rate, discharge_rate=grid_consumption[ems.time_hour])

            # 选择动作
            action =choose_action(ems.state[0], ems.charge_rate, ems.discharge_rate, ems.battery_capacity,
                                  exploration_rate=exploration_rate, q_values=q_values, state=state)

            # 样本计数
            sample_counts[state][action] = sample_counts[state][action] + 1
            # learning_rate = 1 / sample_counts[state][action]

            # 执行动作
            next_state, reward = ems.step(action)

            # 更新q值
            q_values[state][action] = q_values[state][action] + learning_rate*(
                reward + ems.gamma * max_dict(q_values[next_state])[1] - q_values[state][action]
            )

            total_reward += reward
            state = next_state
            states.append(state)
            actions.append(action)
            rewards.append(reward)

            if len(actions)==len(grid_price)-1:
                break

        if episode % 1000 == 0 or episode == num_episode-1:
            print(f"Episode {episode}, Total Reward: {total_reward}")

    q_values_result = pd.DataFrame(q_values).T
    sample_counts_result = pd.DataFrame(sample_counts).T

    print("")
    for action, state in zip(actions, states[:-1]):
        print(f"this state: {state}, this action: {action}")

    money_without_ess, money_with_ess, money_saved = function.money_saved_calculaton(actions, grid_price, grid_consumption, charge_rate=ems.charge_rate)
    print(f"\nMoney without Energy Management: {money_without_ess/1000}$Eu")
    print(f"Money with Energy Management: {money_with_ess/1000}Eu")
    print(f"EMS have saved {money_saved/1000}Eu")

