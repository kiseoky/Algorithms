from collections import deque

r, c, k = map(int, input().split())

room = []
for _ in range(r):
    room.append(list(map(int, input().split())))
walls = set()
w = int(input())
for _ in range(w):
    a, b, t = map(int, input().split())
    a -= 1
    b -= 1
    if t == 0:
        walls.add((a - 0.5, b))
    else:
        walls.add((a, b + 0.5))
heat_list = []
dy = [0, 0, 0, -1, 1]
dx = [0, 1, -1, 0, 0]
check_list = []
for i in range(r):
    for j in range(c):
        d = room[i][j]
        room[i][j] = 0
        if d == 0:
            continue
        if d == 5:
            check_list.append((i, j))
            continue
        room[i][j] = 0
        heat_list.append((i + dy[d], j + dx[d], d))

# 1, 2, 3, 4 -> 우 좌 상 하
wind_r = [[[-1, 0], [0, 1]], [[0, 1]], [[1, 0], [0, 1]]]
wind_l = [[[-1, 0], [0, -1]], [[0, -1]], [[1, 0], [0, -1]]]
wind_u = [[[0, -1], [-1, 0]], [[-1, 0]], [[0, 1], [-1, 0]]]
wind_d = [[[0, -1], [1, 0]], [[1, 0]], [[0, 1], [1, 0]]]
wind_dir = [[], wind_r, wind_l, wind_u, wind_d]
for cnt in range(1, 101):
    queue = deque()
    for i, heat in enumerate(heat_list):
        queue.append((i, heat[0], heat[1], heat[2], 5))
    visited = set()
    while queue:
        h, y, x, d, v = queue.popleft()
        room[y][x] += v

        if v > 1:
            for i in range(3):
                ny = y
                nx = x
                add_flag = True
                for d_y, d_x in wind_dir[d][i]:
                    for _ in range(2):
                        ny += d_y * 0.5
                        nx += d_x * 0.5
                        if not (0 <= ny < r and 0 <= nx < c) or (h, ny, nx) in visited or (ny, nx) in walls:
                            add_flag = False
                            break
                if add_flag:
                    visited.add((h, ny, nx))
                    queue.append((h, int(ny), int(nx), d, v - 1))

    calc = set()
    q = deque()
    for i in range(r):
        for j in range(c):
            for d in range(4):
                ni = i
                nj = j
                for _ in range(2):
                    ni += dy[d] * 0.5
                    nj += dx[d] * 0.5
                    if not (0 <= ni < r and 0 <= nj < c) or ((i, j), (ni, nj)) in calc or (ni, nj) in walls:
                        break
                else:
                    ni = int(ni)
                    nj = int(nj)
                    diff = abs(room[ni][nj] - room[i][j]) // 4
                    if diff < 1:
                        continue
                    if room[ni][nj] > room[i][j]:
                        diff *= -1
                    q.append((ni, nj, diff))
                    q.append((i, j, -diff))
                    calc.add(((i, j), (ni, nj)))
                    calc.add(((ni, nj), (i, j)))

    while q:
        y, x, val = q.popleft()
        room[y][x] += val

    for i in range(r):
        for j in range(c):
            if i == 0 or j == 0 or i == r - 1 or j == c - 1:
                if room[i][j] > 0:
                    room[i][j] -= 1

    if all(room[y][x] >= k for y, x in check_list):
        print(cnt)
        break
else:
    print(101)
"""
7 8 1
0 0 0 0 0 0 0 0
0 0 0 0 4 0 0 0
0 0 0 0 0 0 0 0
0 0 5 5 0 0 0 0
0 0 0 0 0 5 0 0
0 0 0 0 0 0 0 0
0 0 0 0 3 0 0 0
3
4 4 1
5 4 0
5 6 0
"""
