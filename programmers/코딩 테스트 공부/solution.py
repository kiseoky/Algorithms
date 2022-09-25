// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/118668

def solution(alp, cop, problems):
    dp = [[987654321] * 300 for i in range(300)]
    targetAlp = max(problems, key=lambda x: x[0])[0]
    targetCop = max(problems, key=lambda x: x[1])[1]
    alp = min(alp,targetAlp)
    cop = min(cop,targetCop)
    dp[alp][cop] = 0
    for i in range(alp, targetAlp + 1):
        for j in range(cop, targetCop + 1):

            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i][j])
            availables = [p for p in problems if p[0] <= i and p[1] <= j]

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in availables:
                next_alp, next_cop = min(targetAlp, i + alp_rwd), min(targetCop, j+cop_rwd)
                dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)

    return dp[targetAlp][targetCop]