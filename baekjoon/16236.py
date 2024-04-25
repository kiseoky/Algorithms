from collections import deque

n = int(input())
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))


def bfs(lv):
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    ret = []
    q = deque()
    for i in range(n):
        for j in range(n):
            if room[i][j] == 9:
                q.append((i, j, lv, 0))
                room[i][j] = 0
    visited = set()
    while q:
        y, x, lv, d = q.popleft()
        if 0 < room[y][x] < lv:
            if ret and ret[-1][2] < d:
                break
            ret.append((y, x, d))
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not (0 <= ny < n and 0 <= nx < n) or (ny, nx) in visited or room[ny][nx] > lv:
                continue
            visited.add((ny, nx))
            q.append((ny, nx, lv, d + 1))
    if not ret:
        return False
    return sorted(ret)[0]


lv = 2
cnt = 0
sec = 0
while True:
    result = bfs(lv)
    if not result:
        break
    y, x, d = result
    room[y][x] = 9
    cnt += 1
    if lv == cnt:
        lv += 1
        cnt = 0
    sec += d
print(sec)
