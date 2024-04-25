"""
a, b 선행조건.
a가 b보다 먼저 학습되어야 한다.
heapq를 이용해 매번 가장 작은 값 pop.

오답 이유
- a b
- c b
처럼 같은 b를 갖는 경우를 고려하지 않았음.
b는 a, c를 모두 학습한 이후에 heapq에 push해야 함.
"""
import heapq
from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(list)
s = set()
rd = defaultdict(set)
for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    s.add(b)
    rd[b].add(a)

pq = []
pushed = set()
for i in range(1, n + 1):
    if i in s:
        continue

    heapq.heappush(pq, i)
    pushed.add(i)

answer = []
while pq:
    idx = heapq.heappop(pq)
    answer.append(idx)

    if idx in d:
        for v in d[idx]:
            if idx in rd[v]:
                rd[v].remove(idx)
            if v in pushed or len(rd[v]) > 0:
                continue

            heapq.heappush(pq, v)
            pushed.add(v)

print(*answer)

"""
4 2
4 2
3 2
"""