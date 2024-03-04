nums = [0] + list(map(int, input().split()))[:-1]
n = len(nums) - 1
fours = [0] + [1, 2, 3, 4] * 2


def get_cost(a, b):
    if a == 0:
        return 2
    if a == b:
        return 1
    if abs(a - b) == 2:
        return 4
    return 3


# dp[level][left, right] = [(left, right, val), (left, right, val)]
# dp[i][0] = min(dp[i-1][0][2] + get_cost(dp[i-1][0][0], nums[i]), dp[i-1][1][2] + get_cost(dp[i-1][1][0], nums[i]))
# dp = [[[0, 0, 0] for _ in range(2)] for _ in range(n + 1)]
#
# print(dp[0][0])
# for i in range(1, n + 1):
#     if dp[i - 1][0][2] + get_cost(dp[i - 1][0][0], nums[i]) < dp[i - 1][1][2] + get_cost(dp[i - 1][1][0], nums[i]):
#         dp[i][0] = [dp[i-1][0][1], dp[i-1]]
