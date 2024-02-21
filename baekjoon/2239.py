puz = []
col = [set() for _ in range(9)]
row = [set() for _ in range(9)]
block = [[set() for _ in range(3)] for _ in range(3)]
nums = {i for i in range(1, 10)}
zeros = []

for _ in range(9):
    puz.append([int(x) for x in input()])


for i in range(9):
    for j in range(9):
        if puz[i][j] == 0:
            zeros.append((i, j))
        row[i].add(puz[i][j])
        col[j].add(puz[i][j])
        block[i//3][j//3].add(puz[i][j])


def set_values(y, x, value):
    row[y].add(value)
    col[x].add(value)
    block[y // 3][x // 3].add(value)
    puz[y][x] = value


def rm_values(y, x, value):
    row[y].remove(value)
    col[x].remove(value)
    block[y // 3][x // 3].remove(value)
    puz[y][x] = 0


def dfs(idx):
    if idx >= len(zeros):
        for p in puz:
            print(*p, sep='')
        return True
    y, x = zeros[idx]
    cands = nums - row[y] - col[x] - block[y//3][x//3]

    for cand in sorted(cands):
        set_values(y, x, cand)
        if dfs(idx+1):
            return True
        rm_values(y, x, cand)


dfs(0)
