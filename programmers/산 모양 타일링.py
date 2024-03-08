# 주의할 점: %10007을 마지막에 한번만 해주면 수가 너무 커져서 시간초과 발생
# DP 풀 때 dfs 탐색 모양을 그려보면 식을 찾기가 더 쉬운 것 같다.

def solution(n, tops):
    answer = 0
    dp1 = [0] * n
    dp2 = [0] * n

    if tops[0] == 0:
        dp1[0] = 3
        dp2[0] = 2
    else:
        dp1[0] = 4
        dp2[0] = 3

    for i in range(1, n):
        if tops[i] == 0:
            dp1[i] = (dp1[i - 1] * 2 + dp2[i - 1]) % 10007
            dp2[i] = (dp1[i - 1] + dp2[i - 1]) % 10007
        else:
            dp1[i] = (dp1[i - 1] * 3 + dp2[i - 1]) % 10007
            dp2[i] = (dp1[i - 1] * 2 + dp2[i - 1]) % 10007

    return dp1[-1]