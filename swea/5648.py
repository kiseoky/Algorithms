from collections import defaultdict

t = int(input())
dy = [0.5, -0.5, 0, 0]
dx = [0, 0, -0.5, 0.5]

for tc in range(1, t + 1):
    n = int(input())
    arr = []
    answer = 0
    for _ in range(n):
        x, y, d, k = map(int, input().split())
        arr.append([x, y, d, k, True])

    for _ in range(4001):
        for i, (x, y, d, k, valid) in enumerate(arr):
            if not valid:
                continue
            nx = x + dx[d]
            ny = y + dy[d]
            arr[i] = [nx, ny, d, k, valid]
        dic = defaultdict(list)
        for i, (x, y, d, k, valid) in enumerate(arr):
            if not valid:
                continue
            dic[(x, y)].append((i, k))

        for l in dic.values():
            if len(l) <= 1:
                continue
            for i, k in l:
                answer += k
                arr[i][-1] = False
    print(f"#{tc} {answer}")


"""
2
2
1 1 3 1
4 1 2 1
2
-1000 -1000 3 1
1000 1000 1 1
"""