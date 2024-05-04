# 1. is_pal 재귀 -> 반복문으로 변경하여 최적화 후 통과
# 2. 문자열 slicing 로직(O(n)) 없애고 index 이용하도록 변경

import math
s = input()
n = len(s)


def is_pal(s, x, y):
    n = y-x+1
    for i in range(math.ceil(n/2)):
        if s[x+i] != s[y-i-1]:
            return False
    return True

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n+1):
    # get min
    mx = 10e9
    for j in range(i):
        if dp[j][i - j] != 0 and mx > dp[j][i-j]:
            mx = dp[j][i - j]
    if i == 0:
        mx = 0
    if mx == 10e9:
        continue

    for k in range(1, n - i+1):
        if is_pal(s, i, i+k):
            dp[i][k] = mx + 1

print(mx)
