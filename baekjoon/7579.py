n, m = map(int, input().split())

memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
memo = {}
# 문제점. k까지 memo 하면 겹치는 경우가 없을 것 같다. 아마 시간초과 날듯..?
# memo[(0, 0)]에 답이 들어가 버린다.


def disable_app(k, mem):
    ret = 10e9

    if mem >= m:
        memo[(k, mem)] = 0
        return memo[(k, mem)]

    if (k, mem) in memo:
        return memo[(k, mem)]

    # M을 달성하지 못하고 n번째 까지 온 경우
    if k >= n:
        return ret

    ret = min(ret, disable_app(k + 1, mem + memories[k]) + costs[k])
    ret = min(ret, disable_app(k + 1, mem))

    memo[(k, mem)] = ret
    return memo[(k, mem)]


print(disable_app(0, 0))
