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

运行结果如下（仿真一周）：

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
    this state: (20, 125), this action: use_grid
    this state: (20, 133), this action: use_grid
    this state: (20, 149), this action: use_grid
    this state: (20, 169), this action: discharge
    this state: (19, 241), this action: discharge
    this state: (18, 248), this action: discharge
    this state: (17, 217), this action: discharge
    this state: (16, 187), this action: discharge
    this state: (16, 175), this action: discharge
    this state: (15, 153), this action: discharge
    this state: (14, 148), this action: charge
    this state: (19, 142), this action: use_grid
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
    this state: (20, 125), this action: use_grid
    this state: (20, 133), this action: use_grid
    this state: (20, 149), this action: use_grid
    this state: (20, 169), this action: discharge
    this state: (19, 241), this action: discharge
    this state: (18, 248), this action: discharge
    this state: (17, 217), this action: discharge
    this state: (16, 187), this action: discharge
    this state: (16, 175), this action: discharge
    this state: (15, 153), this action: discharge
    this state: (14, 148), this action: charge
    this state: (19, 142), this action: use_grid
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
    this state: (20, 125), this action: use_grid
    this state: (20, 133), this action: use_grid
    this state: (20, 149), this action: use_grid
    this state: (20, 169), this action: discharge
    this state: (19, 241), this action: discharge
    this state: (18, 248), this action: discharge
    this state: (17, 217), this action: discharge
    this state: (16, 187), this action: discharge
    this state: (16, 175), this action: discharge
    this state: (15, 153), this action: discharge
    this state: (14, 148), this action: charge
    this state: (19, 142), this action: use_grid
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
    this state: (20, 125), this action: use_grid
    this state: (20, 133), this action: use_grid
    this state: (20, 149), this action: use_grid
    this state: (20, 169), this action: discharge
    this state: (19, 241), this action: discharge
    this state: (18, 248), this action: discharge
    this state: (17, 217), this action: discharge
    this state: (16, 187), this action: discharge
    this state: (16, 175), this action: discharge
    this state: (15, 153), this action: discharge
    this state: (14, 148), this action: charge
    this state: (19, 142), this action: use_grid
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
    this state: (20, 125), this action: use_grid
    this state: (20, 133), this action: use_grid
    this state: (20, 149), this action: use_grid
    this state: (20, 169), this action: discharge
    this state: (19, 241), this action: discharge
    this state: (18, 248), this action: discharge
    this state: (17, 217), this action: discharge
    this state: (16, 187), this action: discharge
    this state: (16, 175), this action: discharge
    this state: (15, 153), this action: discharge
    this state: (14, 148), this action: charge
    this state: (19, 142), this action: use_grid
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
    this state: (20, 125), this action: use_grid
    this state: (20, 133), this action: use_grid
    this state: (20, 149), this action: use_grid
    this state: (20, 169), this action: discharge
    this state: (19, 241), this action: discharge
    this state: (18, 248), this action: discharge
    this state: (17, 217), this action: discharge
    this state: (16, 187), this action: discharge
    this state: (16, 175), this action: discharge
    this state: (15, 153), this action: discharge
    this state: (14, 148), this action: charge
    this state: (19, 142), this action: use_grid
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
    Money without Energy Management: 33852Eu
    Money with Energy Management: 31816Eu
    EMS have saved 2036Eu
    2036


结果分析
1. 阈值策略只是可以做到在低电价的时候充电,无法做到能量的调节和调度。
2. 并且在电量满载的情况下，不知道去放电而去使用市电。
3. 尽管能量储存在电池中，但是其省钱增益为负数。

## 强化学习策略

强化学习策略可以很好地去解决这些问题，能做到在电池中所冲的电过剩且无法使用的情况。

运行结果如下（仿真一周）：

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
    this state: (0, 142), this action: use_grid
    this state: (0, 151), this action: charge
    this state: (5, 169), this action: discharge
    this state: (4, 198), this action: discharge
    this state: (3, 240), this action: discharge
    this state: (2, 227), this action: discharge
    this state: (0, 166), this action: use_grid
    this state: (0, 147), this action: use_grid
    this state: (0, 148), this action: use_grid
    this state: (0, 132), this action: use_grid
    this state: (0, 132), this action: use_grid
    this state: (0, 125), this action: use_grid
    this state: (0, 121), this action: use_grid
    this state: (0, 125), this action: use_grid
    this state: (0, 133), this action: charge
    this state: (5, 149), this action: discharge
    this state: (4, 169), this action: discharge
    this state: (3, 241), this action: discharge
    this state: (2, 248), this action: discharge
    this state: (1, 217), this action: discharge
    this state: (0, 187), this action: discharge
    this state: (0, 175), this action: use_grid
    this state: (0, 153), this action: use_grid
    this state: (0, 148), this action: use_grid
    this state: (0, 142), this action: use_grid
    this state: (0, 151), this action: charge
    this state: (5, 169), this action: discharge
    this state: (4, 198), this action: discharge
    this state: (3, 240), this action: discharge
    this state: (2, 227), this action: discharge
    this state: (0, 166), this action: use_grid
    this state: (0, 147), this action: use_grid
    this state: (0, 148), this action: use_grid
    this state: (0, 132), this action: use_grid
    this state: (0, 132), this action: use_grid
    this state: (0, 125), this action: use_grid
    this state: (0, 121), this action: use_grid
    this state: (0, 125), this action: use_grid
    this state: (0, 133), this action: charge
    this state: (5, 149), this action: discharge
    this state: (4, 169), this action: discharge
    this state: (3, 241), this action: discharge
    this state: (2, 248), this action: discharge
    this state: (1, 217), this action: discharge
    this state: (0, 187), this action: discharge
    this state: (0, 175), this action: use_grid
    this state: (0, 153), this action: use_grid
    this state: (0, 148), this action: use_grid
    this state: (0, 142), this action: use_grid
    this state: (0, 151), this action: charge
    this state: (5, 169), this action: discharge
    this state: (4, 198), this action: use_grid
    this state: (4, 240), this action: discharge
    this state: (3, 227), this action: discharge
    this state: (1, 166), this action: use_grid
    this state: (1, 147), this action: use_grid
    this state: (1, 148), this action: discharge
    this state: (0, 132), this action: use_grid
    this state: (0, 132), this action: use_grid
    this state: (0, 125), this action: use_grid
    this state: (0, 121), this action: use_grid
    this state: (0, 125), this action: use_grid
    this state: (0, 133), this action: charge
    this state: (5, 149), this action: discharge
    this state: (4, 169), this action: discharge
    this state: (3, 241), this action: discharge
    this state: (2, 248), this action: discharge
    this state: (1, 217), this action: discharge
    this state: (0, 187), this action: use_grid
    this state: (0, 175), this action: use_grid
    this state: (0, 153), this action: use_grid
    this state: (0, 148), this action: use_grid
    this state: (0, 142), this action: charge
    this state: (5, 151), this action: charge
    this state: (10, 169), this action: discharge
    this state: (9, 198), this action: use_grid
    this state: (9, 240), this action: discharge
    this state: (8, 227), this action: discharge
    this state: (6, 166), this action: use_grid
    this state: (6, 147), this action: discharge
    this state: (3, 148), this action: charge
    this state: (8, 132), this action: discharge
    this state: (7, 132), this action: discharge
    this state: (6, 125), this action: discharge
    this state: (5, 121), this action: discharge
    this state: (4, 125), this action: discharge
    this state: (3, 133), this action: use_grid
    this state: (3, 149), this action: discharge
    this state: (2, 169), this action: use_grid
    this state: (2, 241), this action: discharge
    this state: (1, 248), this action: discharge
    this state: (0, 217), this action: use_grid
    this state: (0, 187), this action: use_grid
    this state: (0, 175), this action: use_grid
    this state: (0, 153), this action: use_grid
    this state: (0, 148), this action: use_grid
    this state: (0, 142), this action: use_grid
    this state: (0, 151), this action: charge
    this state: (5, 169), this action: discharge
    this state: (4, 198), this action: discharge
    this state: (3, 240), this action: discharge
    this state: (2, 227), this action: discharge
    this state: (0, 166), this action: use_grid
    this state: (0, 147), this action: use_grid
    this state: (0, 148), this action: use_grid
    this state: (0, 132), this action: use_grid
    this state: (0, 132), this action: use_grid
    this state: (0, 125), this action: use_grid
    this state: (0, 121), this action: use_grid
    this state: (0, 125), this action: charge
    this state: (5, 133), this action: use_grid
    this state: (5, 149), this action: discharge
    this state: (4, 169), this action: discharge
    this state: (3, 241), this action: discharge
    this state: (2, 248), this action: discharge
    this state: (1, 217), this action: discharge
    this state: (0, 187), this action: discharge
    this state: (0, 175), this action: use_grid
    this state: (0, 153), this action: use_grid
    this state: (0, 148), this action: use_grid
    this state: (0, 142), this action: use_grid
    this state: (0, 151), this action: charge
    this state: (5, 169), this action: discharge
    this state: (4, 198), this action: discharge
    this state: (3, 240), this action: discharge
    this state: (2, 227), this action: discharge
    this state: (0, 166), this action: use_grid
    this state: (0, 147), this action: use_grid
    this state: (0, 148), this action: use_grid
    this state: (0, 132), this action: use_grid
    this state: (0, 132), this action: use_grid
    this state: (0, 125), this action: use_grid
    this state: (0, 121), this action: use_grid
    
    Money without Energy Management: 33852Eu
    Money with Energy Management: 29418Eu
    EMS have saved 4434Eu
    4434





