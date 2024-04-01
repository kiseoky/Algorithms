# greedy.
# idea: 좌표와 k에 따라 길은 어차피 정해져있다.
# 이동했을 때 목표 좌표에 도달할 수 없는 좌표를 제외하고 dlru 순서대로 이동
# bfs queue append 뒤 break문이 핵심이다.

## 시간초과 이유 및 주의할점
# 51*51*'uuuu' 배열을 만들어놓고 까먹고 있었는데 이거 때문에 시간초과남.
## 사용하지 않는 변수, 특히 배열은 제출 전 삭제할 것.

from collections import deque


def solution(n, m, x, y, r, c, k):
    dy = [1, 0, 0, -1]
    dx = [0, -1, 1, 0]

    queue = deque()
    queue.append((x, y, ''))

    while queue:
        cy, cx, route = queue.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            dis = abs(r - ny) + abs(c - nx)
            d = k - 1 - len(route)
            if 1 <= ny <= n and 1 <= nx <= m and dis <= d and (d - dis) % 2 == 0:
                if dis == 0 and d == 0:
                    return route + "dlru"[i]

                queue.append((ny, nx, route + "dlru"[i]))
                break

    return "impossible"