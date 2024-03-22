from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lab = []
space_cnt = -3
spaces = []
viruses = []
virus_cnt = 0
answer = 0
for i in range(n):
    line = list(map(int, input().split()))
    lab.append(line)

    for j, v in enumerate(line):
        if v == 0:
            space_cnt += 1
            spaces.append((i, j))
        elif v == 2:
            virus_cnt += 1
            viruses.append((i, j))


def bfs(queue):
    affected_cnt = 0
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    visited = set(queue)
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and (ny, nx) not in visited and lab[ny][nx] == 0:
                affected_cnt += 1
                visited.add((ny, nx))
                queue.append((ny, nx))

    return affected_cnt


def set_lab(arr, t):
    for y, x in arr:
        lab[y][x] = t


for comb in combinations(spaces, 3):
    set_lab(comb, 1)
    answer = max(answer, space_cnt - bfs(deque(viruses)))
    set_lab(comb, 0)

print(answer)
