import numpy as np

class EnergyManagementMDP:
    def __init__(self, battery_capacity, max_charge_rate, max_discharge_rate, grid_price, discount_factor):
        self.battery_capacity = battery_capacity
        self.max_charge_rate = max_charge_rate
        self.max_discharge_rate = max_discharge_rate
        self.grid_price = grid_price
        self.discount_factor = discount_factor
        self.current_battery_level = None

    def reset(self):
        # 重置状态
        self.current_battery_level = np.random.uniform(0, self.battery_capacity)
        return self.current_battery_level

    def step(self, action):
        # 执行动作并获取奖励和下一个状态
        if action == "charge":
            charge_rate = np.random.uniform(0, self.max_charge_rate)
            self.current_battery_level = min(self.current_battery_level + charge_rate, self.battery_capacity)
        elif action == "discharge":
            discharge_rate = np.random.uniform(0, self.max_discharge_rate)
            self.current_battery_level = max(self.current_battery_level - discharge_rate, 0)
        # 使用市电的情况
        else:
            grid_usage = np.random.uniform(0, self.max_discharge_rate)
            self.current_battery_level = max(self.current_battery_level - grid_usage, 0)

        # 计算奖励
        reward = -action_cost(action, self.grid_price)

        return self.current_battery_level, reward

def action_cost(action, grid_price):
    # 计算动作的成本，这里简化为动作对应的市电成本
    if action == "charge":
        return 0  # 充电不产生额外成本
    elif action == "discharge":
        return grid_price
    else:
        return grid_price  # 使用市电同样需要支付市电成本

def q_learning(mdp, num_episodes, learning_rate, exploration_rate):
    q_values = np.zeros((int(mdp.battery_capacity) + 1, 3))  # 状态空间包括电池电量，动作空间包括充电、放电、使用市电

    for episode in range(num_episodes):
        state = mdp.reset()
        total_reward = 0

        while True:
            # 选择动作，加入探索
            if np.random.rand() < exploration_rate:
                action = np.random.choice(3)  # 0: 充电，1: 放电，2: 使用市电
            else:
                action = np.argmax(q_values[state])

            # 执行动作并获取奖励和下一个状态
            next_state, reward = mdp.step(action)

            # 更新 Q 值
            q_values[state, action] += learning_rate * (
                reward + mdp.discount_factor * np.max(q_values[next_state]) - q_values[state, action]
            )

            total_reward += reward
            state = int(next_state)

            if total_reward < -100:
                break  # 防止无限循环

        if episode % 100 == 0:
            print(f"Episode {episode}, Total Reward: {total_reward}")

    return q_values

# 定义一个简化的MDP
battery_capacity = 100  # 电池容量
max_charge_rate = 5  # 最大充电速率
max_discharge_rate = 5  # 最大放电速率
grid_price = np.random.uniform(0.1, 0.3)  # 实时电价
discount_factor = 0.9  # 折扣因子

energy_mdp = EnergyManagementMDP(battery_capacity, max_charge_rate, max_discharge_rate, grid_price, discount_factor)

# 训练 Q 值
num_episodes = 1000
learning_rate = 0.1
exploration_rate = 0.1

trained_q_values = q_learning(energy_mdp, num_episodes, learning_rate, exploration_rate)

# 打印训练后的 Q 值
print("Trained Q-values:")
print(trained_q_values)
