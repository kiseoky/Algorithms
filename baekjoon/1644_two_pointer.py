##
# 알고리즘 분류에 투 포인터로 되어 있어서 투 포인터로 한번 더 풀어봄
# O(NlogN) -> O(N)
# 투 포인터 유형 문제를 좀 더 풀어봐야겠다.
##
n = int(input())


def eratos(num):
    prime_flags = [1] * (num + 1)
    prime_flags[0] = 0
    prime_flags[1] = 0

    for i in range(2, num + 1):
        if prime_flags[i] == 0:
            continue
        prime_flags[i + i::i] = [0] * len(prime_flags[i + i::i])

    return [i for i, flag in enumerate(prime_flags) if flag]


primes = eratos(n)
cnt = 0
p_len = len(primes)

l = 0
r = 0
val = 0

while l <= r <= p_len:
    if val >= n:
        if val == n:
            cnt += 1
            print(l, r)
        val -= primes[l]
        l += 1
    else:
        if r == p_len:
            break
        val += primes[r]
        r += 1

print(cnt)
