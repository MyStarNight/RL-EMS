import environment
import function
import train
import pandas as pd
import numpy as np

days = 7
new_price_dict = {}
new_consumption_dict = {}
for hour in range(1, int(days * 24) + 2):
    new_price_dict[hour] = train.price_dict[int(hour % 24)] if hour % 24 != 0 else train.price_dict[24]
    new_consumption_dict[hour] = train.consumption_dict[int(hour % 24)] if hour % 24 != 0 else train.consumption_dict[24]

# 获取电价、损耗
grid_price, grid_consumption = function.processing_data(new_price_dict, new_consumption_dict)
battery_dict = train.battery_dict

# 计算阈值，采用均值的方式
# threshold = round(np.average(pd.Series(grid_price).values))
threshold = np.median(pd.Series(grid_price).values)

# ems，启动！
ems = environment.EMS_MDP(
    grid_price=grid_price,
    battery_capacity=battery_dict["capacity"],
    max_charge_rate=battery_dict["max_charge_rate"],
    max_discharge_rate=battery_dict["max_discharge_rate"]
)

# 重置EMS，回到初始状态
state = ems.reset(energy_start=battery_dict["start_state"])
total_reward = 0

states = [state]
actions = []
rewards = []
while True:
    # 设定当前状态下的充放电功率
    ems.charge_discharge(charge_rate=ems.max_charge_rate, discharge_rate=grid_consumption[ems.time_hour])

    # 动作选择
    if ems.state[1] < threshold and ems.state[0]+ems.charge_rate <= ems.battery_capacity :
        action = 'charge'
    elif ems.state[1] >= threshold and ems.state[0]-ems.discharge_rate>=0:
        action = 'discharge'
    else:
        action = 'use_grid'

    next_state, reward = ems.step(action)
    total_reward += reward
    state = next_state
    states.append(state)
    actions.append(action)
    rewards.append(reward)

    if len(actions) == len(grid_price)-1:
        break

for action, state in zip(actions, states[:-1]):
    print(f"this state: {state}, this action: {action}")

money_without_ess, money_with_ess, money_saved, money_without_ess_list, money_with_ess_list = function.money_saved_calculaton(actions, grid_price, grid_consumption, charge_rate=ems.charge_rate)
print(f"\nMoney without Energy Management: {money_without_ess}Eu")
print(f"Money with Energy Management: {money_with_ess}Eu")
print(f"EMS have saved {money_saved}Eu")
print(total_reward)
