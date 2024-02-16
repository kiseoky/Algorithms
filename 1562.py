n = int(input())


def solution(n):
    able = n - 10
    if able < 0:
        return 0

    dp = [[0] * (able + 1) for _ in range(10)]

    dp[0][1] = 1
    dp[9][1] = 1
    for i in range(1, 9):
        dp[i][1] = 2

    for i in range(2, able + 1):
        for j in range(10):
            if j == 0:
                dp[j][i] = dp[1][i - 1]
            elif j == 9:
                dp[j][i] = dp[8][i - 1]
            else:
                dp[j][i] = (dp[j - 1][i - 1] + dp[j + 1][i - 1]) % int(10e9)

    print(*dp, sep="\n")
    ans = 0
    for i in range(able + 1):
        l, r = i, able - i
        l_val, r_val = dp[9][l] or 1, dp[0][r] or 1
        ans = (ans + l_val * r_val) % int(10e9)

    return ans


print(solution(n))
# summed = 0
# for i in range(1, 41):
# summed += solution(i)
# print(summed)
