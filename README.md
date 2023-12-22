# README

This is a repo for energy management system with reinforcement learning.

`environment.py` is for the battery simulation.

`function.py` is for the whole repo.

`train.py` is for the reinforcement learning training.


# 运行

运行强化学习优化策略： `python train.py`

运行阈值策略：`python ess_without_rl.py`

# 仿真结果

## 阈值策略

从目前的结果来看，阈值策略并没有想象的那么聪明.

运行结果如下：

    this state: (0, 125), this action: charge
    this state: (5, 133), this action: charge
    this state: (10, 149), this action: charge
    this state: (15, 169), this action: discharge
    this state: (14, 241), this action: discharge
    this state: (13, 248), this action: discharge
    this state: (12, 217), this action: discharge
    this state: (11, 187), this action: discharge
    this state: (11, 175), this action: discharge
    this state: (10, 153), this action: discharge
    this state: (9, 148), this action: charge
    this state: (14, 142), this action: charge
    this state: (19, 151), this action: discharge
    this state: (17, 169), this action: discharge
    this state: (16, 198), this action: discharge
    this state: (15, 240), this action: discharge
    this state: (14, 227), this action: discharge
    this state: (12, 166), this action: discharge
    this state: (10, 147), this action: charge
    this state: (15, 148), this action: charge
    this state: (20, 132), this action: use_grid
    this state: (20, 132), this action: use_grid
    this state: (20, 125), this action: use_grid
    this state: (20, 121), this action: use_grid
    
    Money without Energy Management: 4836Eu
    Money with Energy Management: 6898Eu
    EMS have saved -2062Eu
    -2062

结果分析
1. 阈值策略只是可以做到在低电价的时候充电,无法做到能量的调节和调度。
2. 并且在电量满载的情况下，不知道去放电而去使用市电。
3. 尽管能量储存在电池中，但是其省钱增益为负数。

## 强化学习策略

强化学习策略可以很好地去解决这些问题，能做到在电池中所冲的电过剩且无法使用的情况。

运行结果如下（一共运行了7*24h， 截取其中一部分）：

    this state: (0, 125), this action: use_grid
    this state: (0, 133), this action: charge
    this state: (5, 149), this action: charge
    this state: (10, 169), this action: discharge
    this state: (9, 241), this action: discharge
    this state: (8, 248), this action: discharge
    this state: (7, 217), this action: discharge
    this state: (6, 187), this action: use_grid
    this state: (6, 175), this action: discharge
    this state: (5, 153), this action: discharge
    this state: (4, 148), this action: use_grid
    this state: (4, 142), this action: use_grid
    this state: (4, 151), this action: charge
    this state: (9, 169), this action: discharge
    this state: (8, 198), this action: discharge
    this state: (7, 240), this action: discharge
    this state: (6, 227), this action: discharge
    this state: (4, 166), this action: discharge
    this state: (2, 147), this action: charge
    this state: (7, 148), this action: discharge
    this state: (6, 132), this action: discharge
    this state: (5, 132), this action: use_grid
    this state: (5, 125), this action: discharge
    this state: (4, 121), this action: charge
    this state: (9, 125), this action: discharge
    this state: (8, 133), this action: discharge
    this state: (7, 149), this action: discharge
    this state: (6, 169), this action: discharge
    this state: (5, 241), this action: discharge
    this state: (4, 248), this action: discharge
    this state: (3, 217), this action: discharge
    this state: (2, 187), this action: use_grid
    this state: (2, 175), this action: discharge
    this state: (1, 153), this action: discharge
    this state: (0, 148), this action: use_grid

    Money without Energy Management: 33852Eu
    Money with Energy Management: 29418Eu
    EMS have saved 4434Eu
    4434



