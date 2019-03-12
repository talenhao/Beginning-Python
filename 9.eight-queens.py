# -*- coding: UTF-8 -*-

"""
 @Author: 郝天飞/Talen Hao (talenhao@gmail.com)
 @Site: talenhao.github.io
 @Since: 3/12/19 3:19 PM
"""

name = "study"


def conflict(state, nextX):
    nextY = len(state)
    for queen_state_i in range(nextY):
        # 在同一列或在斜线上. |y-y| = |x-x|
        if abs(state[queen_state_i] - nextX) in (0, nextY - queen_state_i):
            return True
    return False


# Base case:
def queens_base(num, state):
    for pos in num:
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)


# Recursive Case:
def queens_recursive(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens_recursive(num, state+(pos,)):
                    # pos放前面的原因是pos是按num从小到大的顺序遍历的
                    yield (pos,) + result


def queens(num=8, state=()):
    for pos in range(num):
        # 前提条件:不冲突
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state+(pos,)):
                    yield result + (pos,)


print(list(queens(4, (1, 3, 0))))
print(list(queens_recursive(4)))
