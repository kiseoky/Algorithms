import sys
import heapq

n, e = map(int, sys.stdin.readline().strip().split())
roads = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    roads[a].append((b, c))
    roads[b].append((a, c))

a, b = list(map(int, input().split()))


def get_min_distance(start, target):
    dis = [10e9] * (n + 1)
    dis[start] = 0
    queue = [(0, start)]

    while queue:
        cost, node = heapq.heappop(queue)
        if node == target:
            return cost
        for nxt_node, nxt_cost in roads[node]:
            if dis[nxt_node] > dis[node] + nxt_cost:
                dis[nxt_node] = dis[node] + nxt_cost
                heapq.heappush(queue, (dis[node] + nxt_cost, nxt_node))

    return dis[target]


answer = min(get_min_distance(1, a) + get_min_distance(a, b) + get_min_distance(b, n),
             get_min_distance(1, b) + get_min_distance(b, a) + get_min_distance(a, n))

print(-1 if answer >= 10e9 else answer)
