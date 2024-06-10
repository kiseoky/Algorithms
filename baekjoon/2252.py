import sys
from collections import deque

n, m = map(int, input().split())
level = [0 for _ in range(n + 1)]
s = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    s[a].append(b)
    level[b] += 1

answer = []

q = deque()
for i in range(1, n+1):
    if level[i] == 0:
        q.append(i)

while q:
    val = q.popleft()
    answer.append(val)
    for node in s[val]:
        level[node] -= 1
        if level[node] == 0:
            q.append(node)

print(*answer)
