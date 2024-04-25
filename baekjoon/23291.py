from collections import deque

n, K = map(int, input().split())
arr = deque([[] for _ in range(n)])
fishes = list(map(int, input().split()))

for i in range(n):
    arr[i].append(fishes[i])

cnt = 1
while True:
    min_v = min(fishes)

    for i in range(n):
        if arr[i][0] == min_v:
            arr[i][0] += 1

    arr[1].append(arr.popleft()[0])

    i = 0
    h = 2
    w = 1
    nn = n
    while w + h <= len(arr):
        res = []
        for _ in range(w):
            res.append(arr.popleft())
            nn -= 1

        for j in range(h):
            for k in range(w):
                arr[j].append(res[w - k - 1][j])
        i += 1
        if i % 2 == 0:
            h += 1
        else:
            w += 1

    calc_set = set()
    q = []
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]

                if not (0 <= ni < len(arr) and 0 <= nj < len(arr[ni]) and ((i, j), (ni, nj)) not in calc_set):
                    continue
                if abs(arr[i][j] - arr[ni][nj]) < 5:
                    continue
                v = abs(arr[i][j] - arr[ni][nj]) // 5
                if arr[i][j] > arr[ni][nj]:
                    v *= -1
                q.append((i, j, v))
                q.append((ni, nj, -v))
                calc_set.add(((i, j), (ni, nj)))
                calc_set.add(((ni, nj), (i, j)))

    while q:
        y, x, v = q.pop()
        arr[y][x] += v

    a = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            a.append(arr[i][j])

    arr = deque([[] for _ in range(len(a))])
    for i in range(len(a)):
        arr[i].append(a[i])

    for i in range(n // 2):
        a = arr.popleft()
        arr[len(arr) - i - 1] += a

    m = len(arr)
    for _ in range(m // 2):
        a = arr.popleft()[::-1]
        arr[len(arr) - i - 1] += a

    calc_set = set()
    q = []
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]

                if not (0 <= ni < len(arr) and 0 <= nj < len(arr[ni]) and ((i, j), (ni, nj)) not in calc_set):
                    continue
                if abs(arr[i][j] - arr[ni][nj]) < 5:
                    continue
                v = abs(arr[i][j] - arr[ni][nj]) // 5
                if arr[i][j] > arr[ni][nj]:
                    v *= -1
                q.append((i, j, v))
                q.append((ni, nj, -v))
                calc_set.add(((i, j), (ni, nj)))
                calc_set.add(((ni, nj), (i, j)))

    while q:
        y, x, v = q.pop()
        arr[y][x] += v

    fishes = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            fishes.append(arr[i][j])

    if max(fishes) - min(fishes) <= K:
        print(cnt)
        break

    arr = deque([[] for _ in range(len(fishes))])
    for i in range(len(fishes)):
        arr[i].append(fishes[i])

    cnt += 1
