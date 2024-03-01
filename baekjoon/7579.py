n, m = map(int, input().split())

memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))


def solution():
    # dp[i][j] = i번째까지 확인했을 때, j비용으로 얻을 수 있는 최대 메모리
    dp = [[0] * 10001 for _ in range(n + 1)]

    total_cost = sum(costs)

    for i in range(1, n + 1):
        for j in range(total_cost + 1):
            if j >= costs[i]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - costs[i]] + memories[i])
            dp[i][j] = max(dp[i][j], dp[i - 1][j])

    for i in range(total_cost + 1):
        if dp[n][i] >= m:
            return i

    return -1


print(solution())
