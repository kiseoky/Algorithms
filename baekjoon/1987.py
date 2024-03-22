# 특이점. set으로는 시간초과, visited 배열로는 통과.
# set이 이론적으로는 o(1)이라고 하더라도 시간복잡도에 민감한 문제에선 배열을 쓸수있으면 쓰는게 좋겠다.
import sys

r, c = map(int, sys.stdin.readline().strip().split())

board = []
for _ in range(r):
    board.append(sys.stdin.readline().strip())
al_set = [False]*100
answer = 0

dy = [0, 1, -1, 0]
dx = [-1, 0, 0, 1]

a_ord = ord('A')
def dfs(y, x, depth):
    global answer
    answer = max(answer, depth)

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < r and 0 <= nx < c and not al_set[ord(board[ny][nx])-a_ord]:
            al_set[ord(board[ny][nx])-a_ord] = True
            dfs(ny, nx, depth+1)
            al_set[ord(board[ny][nx])-a_ord] = False


al_set[ord(board[0][0])-a_ord] = True
dfs(0, 0, 1)

print(answer)


