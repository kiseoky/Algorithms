from collections import deque

n = int(input())
k = int(input())

board = [[0] * (n + 2) for _ in range(n + 2)]

for i in range(n + 2):
    for j in range(n + 2):
        if i == 0 or j == 0 or i == n + 1 or j == n + 1:
            board[i][j] = 1
board[1][1] = 1

for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 2

l = int(input())
m = {}
for _ in range(l):
    x, d = input().split()
    m[int(x)] = d

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

head = [1, 1]
tail = [1, 1]
queue = deque()
d, t = 1, 0
while True:
    if t in m:
        if m[t] == 'L':
            d = (d - 1) % 4
        else:
            d = (d + 1) % 4

    head[0] += dy[d]
    head[1] += dx[d]
    queue.append(head[:])
    t += 1

    if (not (1 <= head[0] <= n and 1 <= head[1] <= n)) or board[head[0]][head[1]] == 1:
        break

    if board[head[0]][head[1]] != 2:
        board[tail[0]][tail[1]] = 0
        tail = queue.popleft()

    board[head[0]][head[1]] = 1

print(t)
