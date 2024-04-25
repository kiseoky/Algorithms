import heapq

t = int(input())
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for tc in range(1, t + 1):
    n, m, k = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    active_dict = {}
    passive_dict = {}
    dead_set = set()

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                continue
            passive_dict[(i, j)] = [grid[i][j], 0]

    for _ in range(1, k + 1):
        active_tmp = {}
        passive_tmp = {}
        queue = []
        for i, j in list(passive_dict.keys()):
            passive_dict[(i, j)][1] += 1
            h, n = passive_dict[(i, j)]
            if h == n:
                heapq.heappush(queue, (-h, i, j))
                del passive_dict[(i, j)]

        while queue:
            h, i, j = heapq.heappop(queue)
            h *= -1
            if (i, j) not in active_dict and (i, j) not in active_tmp:
                active_tmp[(i, j)] = [h, 0]

        for i, j in list(active_dict.keys()):
            active_dict[(i, j)][1] += 1
            if active_dict[(i, j)][1] == 1:
                for idx in range(4):
                    ny = i + dy[idx]
                    nx = j + dx[idx]
                    if (ny, nx) in passive_dict or (ny, nx) in active_dict or (ny, nx) in dead_set or (
                            ny, nx) in active_tmp or (ny, nx) in passive_tmp:
                        continue
                    passive_tmp[(ny, nx)] = [active_dict[(i, j)][0], 0]
            h, n = active_dict[(i, j)]
            if h == n:
                dead_set.add((i, j))
                del active_dict[(i, j)]

        active_dict.update(active_tmp)
        passive_dict.update(passive_tmp)
    print(f"#{tc} {len(passive_dict)+len(active_dict)}")
