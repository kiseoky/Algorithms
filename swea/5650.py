def change_dir(block, d):
    if block == 1:
        if d == 3:
            return 0
        if d == 2:
            return 1
    elif block == 2:
        if d == 0:
            return 1
        if d == 3:
            return 2
    elif block == 3:
        if d == 1:
            return 2
        if d == 0:
            return 3
    elif block == 4:
        if d == 1:
            return 0
        if d == 2:
            return 3
    return (d + 2) % 4


t = int(input())

for tc in range(t):
    n = int(input())
    board = [[5] * (n + 2)]
    # 한 글자씩 받는 것도 알아 두자.
    for _ in range(n):
        board.append([5] + list(map(int, input().split())) + [5])
    board.append([5] * (n + 2))

    hole = {}
    hole_map = {}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if board[i][j] > 5:
                if board[i][j] in hole:
                    hole_map[(i, j)] = hole[board[i][j]]
                    hole_map[hole[board[i][j]]] = (i, j)
                else:
                    hole[board[i][j]] = (i, j)


    def get_score(y, x, d):
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        score = 0
        cy, cx = y, x
        while True:
            cy += dy[d]
            cx += dx[d]

            if (cy, cx) == (y, x) or board[cy][cx] == -1:
                break

            if 1 <= board[cy][cx] <= 5:
                score += 1
                d = change_dir(board[cy][cx], d)
            elif board[cy][cx] > 5:
                cy, cx = hole_map[(cy, cx)]
        return score

    answer = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] != 0:
                continue
            for d in range(4):
                answer = max(answer, get_score(i, j, d))

    print(f"#{tc+1} {answer}")
