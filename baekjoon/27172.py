import sys
import math

n = int(input())
scores = list(map(int, sys.stdin.readline().strip().split()))
result = {score: 0 for score in scores}

for i, score in enumerate(scores):
    if 1 in result:
        result[1] += 1
        result[score] -= 1

    s = set()
    for num in range(2, math.ceil(math.sqrt(score)) + 1):
        if score % num == 0:
            if num in result and num not in s:
                result[num] += 1
                result[score] -= 1
                s.add(num)
            r = score//num
            if r in result and r not in s:
                s.add(r)
                result[r] += 1
                result[score] -= 1

print(*result.values())
