from bisect import bisect_left

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
acc = [0] + primes[:]

for i in range(1, len(acc)):
    acc[i] += acc[i - 1]

cnt = 0
acc_len = len(acc)
for a in acc:
    bs = bisect_left(acc, a + n)
    if bs >= acc_len or acc[bs] != a + n:
        continue
    cnt += 1

print(cnt)
