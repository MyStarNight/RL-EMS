import environment
import numpy as np
import function

# price: https://www.kaggle.com/datasets/arashnic/electricity-spot-price
# consumption: https://www.kaggle.com/datasets/taranvee/smart-home-dataset-with-weather-information

'''
配置文件信息
'''

# 单位为Euro, 欧元
price_dict = {
    1: 125.120003,
    2: 133.179993,
    3: 148.600006,
    4: 169.429993,
    5: 240.649994,
    6: 247.740005,
    7: 216.690002,
    8: 187.309998,
    9: 174.759995,
    10: 152.619995,
    11: 148.190002,
    12: 142.479996,
    13: 151.259995,
    14: 168.929993,
    15: 197.839996,
    16: 240.160004,
    17: 226.919998,
    18: 166.500000,
    19: 146.570007,
    20: 148.149994,
    21: 131.570007,
    22: 131.619995,
    23: 125.180000,
    24: 121.419998,

}

# 按照每分钟使用的P(kw)进行叠加
consumption_dict = {
    1: 55.09001667,
    2: 42.88416667,
    3: 57.60076667,
    4: 38.39018333,
    5: 73.16496667,
    6: 47.92483334,
    7: 32.22328333,
    8: 21.5026,
    9: 45.40321667,
    10: 88.23483334,
    11: 79.29818334,
    12: 115.0013167,
    13: 125.7233833,
    14: 78.2594,
    15: 76.2767,
    16: 89.09918334,
    17: 115.7258,
    18: 121.8189,
    19: 165.5063167,
    20: 85.87201666,
    21: 56.717,
    22: 46.45626667,
    23: 89.34038334,
    24: 62.64778333,

}

battery_dict = {
    "capacity": 20,
    "max_charge_rate": 5,
    "max_discharge_rate": 5,
    "start_state": 0
    # "start_state": np.random.randint(1, 61)
}

days = 7

if __name__ == '__main__':

    # 延长时间
    new_price_dict = {}
    new_consumption_dict = {}
    for hour in range(1, int(days*24)+2):
        new_price_dict[hour] = price_dict[int(hour%24)] if hour%24 != 0 else price_dict[24]
        new_consumption_dict[hour] = consumption_dict[int(hour%24)] if hour%24 != 0 else consumption_dict[24]
        # new_consumption_dict[hour] = 300

    states, actions, rewards, q_values, sample_counts = function.q_learning_train(
        price_dict=new_price_dict,
        consumption_dict=new_consumption_dict,
        battery_dict=battery_dict,
        num_episode=10000,
        exploration_rate=0.2,
        learning_rate=0.1
    )

