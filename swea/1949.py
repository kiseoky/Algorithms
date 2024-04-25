from collections import deque

t = int(input())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


def copy(arr):
    return [a[:] for a in arr]


for tc in range(1, t + 1):
    n, k = map(int, input().split())
    m = []
    for _ in range(n):
        m.append(list(map(int, input().split())))

    mx = max([m[i][j] for j in range(n) for i in range(n)])
    visited = [[False]*n for _ in range(n)]

    answer = 0


    def dfs(y, x, d, flag, route):
        global answer
        answer = max(answer, d)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not (0 <= ny < n and 0 <= nx < n):
                continue

            if m[ny][nx] >= m[y][x] > m[ny][nx] - k and not flag and not visited[ny][nx]:
                tmp = m[ny][nx]
                m[ny][nx] = m[y][x] - 1
                visited[ny][nx] = True
                dfs(ny, nx, d + 1, True, route+[(ny, nx)])
                m[ny][nx] = tmp
                visited[ny][nx] = False

            if m[ny][nx] < m[y][x] and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx, d + 1, flag, route+[(ny, nx)])
                visited[ny][nx] = False


    for i in range(n):
        for j in range(n):
            if m[i][j] == mx:
                visited[i][j] = True
                dfs(i, j, 1, False, [(i, j)])
                visited[i][j] = False
    print(f"#{tc} {answer}")

"""
1
4 4
8 3 9 5
4 6 8 5
8 1 5 1
4 9 5 5
"""