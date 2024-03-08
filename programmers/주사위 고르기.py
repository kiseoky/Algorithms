# 그냥 계산 시 O(10^10)
# 이분탐색으로 6^5 * log(6^5)

from itertools import combinations
from bisect import bisect_left, bisect_right


def solution(dice):
    n = len(dice)
    combs = list(combinations(range(n), n // 2))

    def roll(idx, comb, res, sums):
        if idx == len(comb):
            sums.append(res)
            return
        for i in range(6):
            roll(idx + 1, comb, res + dice[comb[idx]][i], sums)

    stat = [[0, 0] for _ in range(len(combs))]

    for idx, comb in enumerate(combs):
        a_sums = []
        b_sums = []
        roll(0, comb, 0, a_sums)
        others = [i for i in range(n) if i not in comb]
        roll(0, others, 0, b_sums)
        b_sums.sort()

        for a_sum in a_sums:
            stat[idx][0] += bisect_left(b_sums, a_sum)
            stat[idx][1] += bisect_right(b_sums, a_sum) - bisect_left(b_sums, a_sum)

    answer_idx = max([i for i in range(len(combs))], key=lambda x: stat[x])

    return sorted([i + 1 for i in combs[answer_idx]])

# comb 10C5 = 10^3
# 6^10 = 10^7
