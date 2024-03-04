# 틀렸던 이유
# get_cost 4 -> 1로 가는 경우 고려 안함
# 양발 다 같은 곳에 있는 경우 처리 안함 (2, 2)
# setrecursionlimit 처리 안함 (런타임 에러)

import sys

sys.setrecursionlimit(1000000)

nums = list(map(int, input().split()))[:-1]
n = len(nums)
memo = {}


def get_cost(a, b):
    if a == 0:
        return 2
    if a == b:
        return 1
    if abs(a - b) == 2:
        return 4
    return 3


def step(k, x, y):
    if k == n:
        return 0
    if (k, x, y) in memo:
        return memo[(k, x, y)]

    if nums[k] in (x, y):
        ret = step(k + 1, x, y) + 1
    else:
        ret = step(k + 1, nums[k], y) + get_cost(x, nums[k])
        ret = min(ret, step(k + 1, x, nums[k]) + get_cost(y, nums[k]))
    memo[(k, x, y)] = ret
    memo[(k, y, x)] = ret

    return memo[(k, x, y)]


print(step(0, 0, 0))
