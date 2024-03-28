def solution(cap, n, d, p):
    answer = 0

    d_cap, p_cap = 0, 0
    for i in range(n - 1, -1, -1):
        while d[i] > 0 or p[i] > 0:
            if d[i] > d_cap or p[i] > p_cap:
                d_cap += cap
                p_cap += cap
                answer += (i + 1) * 2

            d_now = min(d[i], d_cap)
            d[i] -= d_now
            d_cap -= d_now

            p_now = min(p[i], p_cap)
            p[i] -= p_now
            p_cap -= p_now

    return answer


# 처음 오답
# 맨 끝부터 배달, 수거하고 pop하며 길이를 더함
# 문제점: 처음에 끝이 0인 경우는 고려했지만 중간에 0이 껴있는 경우는 고려하지 못함.
# 반례 1, 5, [1, 0, 0, 0, 1], [0, 0, 0, 0, 1]
def solution(cap, n, deliveries, pickups):
    answer = 0

    while True:
        p_cnt, d_cnt = 0, 0
        if not deliveries:
            break
        while deliveries[-1] == pickups[-1] == 0:
            deliveries.pop()
            pickups.pop()
        answer += len(pickups) * 2
        for i in range(len(pickups) - 1, -1, -1):
            delivered = min(deliveries[i], cap - d_cnt)
            deliveries[i] -= delivered
            d_cnt += delivered

            picked = min(pickups[i], cap - p_cnt)
            pickups[i] -= picked
            p_cnt += picked

            if deliveries[i] == pickups[i] == 0:
                deliveries.pop()
                pickups.pop()

            if cap == d_cnt == p_cnt:
                break

        if len(pickups) == 0:
            break

    return answer
