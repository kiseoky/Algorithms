arr = [1, 2, 3, 4]


def get_combinations(arr, r):
    ret = []

    def combinations(n_arr, r, idx=0):
        if len(n_arr) == r:
            ret.append(n_arr)
            return
        for i in range(idx + 1, len(arr)):
            combinations(n_arr + [(arr[i], 0)], r, i)
            combinations(n_arr + [(arr[i], 1)], r, i)

    for i in range(len(arr)):
        combinations([(arr[i], 0)], r, i)
        combinations([(arr[i], 1)], r, i)

    return ret

def check_board(board, comb, k):
    for j in range(len(board[0])):
        stack = []
        for i in range(len(board)):
            t = board[i][j]
            if i in comb:
                t = comb[i]
            if stack and stack[-1] == t:
                stack.append(t)
            else:
                stack = [t]
            if len(stack) == k:
                break
        else:
            return False
    return True


def get_answer(board, d, k):
    if check_board(board, [], k):
        return 0
    for i in range(1, k):
        combs = get_combinations(range(d), i)
        for comb in combs:
            n_comb = {}
            for a, b in comb:
                n_comb[a] = b
            if check_board(board, n_comb, k):
                return i

    return k


t = int(input())
for tc in range(1, t + 1):
    d, w, k = map(int, input().split())
    board = []
    for _ in range(d):
        board.append(list(map(int, input().split())))
    print(f"#{tc} {get_answer(board, d, k)}")

"""
1
6 8 6
0 0 1 0 1 0 0 1
0 1 0 0 0 1 1 1
0 1 1 1 0 0 0 0
1 1 1 1 0 0 0 1
0 1 1 0 1 0 0 1
1 0 1 0 1 1 0 1
"""
