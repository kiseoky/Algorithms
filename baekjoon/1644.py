##
# 1. 처음에 에라토스 테네스 체를 안써도 될 줄 알았음.
#     - N=4*10*6, O(NlogN) 이라고 생각해서 괜찮을 줄 알았는데 연산 개수를 직접 세보니 7*10^11
# 2. 중복을 방지하기 위해 set을 썼으나 필요 없었고, 이거때매 틀림
#     - a+n을 찾기 때문에 중복이 있을 수 없음 (a 기준 오른쪽만 검색)
#     - (a, a+n) 짝을 찾았을 때, a+n을 중복 제거 set에 넣으면 안됨. (a+n, a+n+n) 짝이 있을 수 있음
##
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
