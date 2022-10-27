// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/86971

from itertools import combinations


def get_diff(n, wires):
    answer = 987654321
    conn = [[] for i in range(n + 1)]

    for a, b in wires:
        conn[a].append(b)
        conn[b].append(a)

    visited = [False for i in range(n + 1)]

    def dfs(a):
        cnt = 1;
        for b in conn[a]:
            if visited[b]:
                continue
            visited[b] = True
            cnt += dfs(b)

            visited[b] = False
        return cnt

    visited[1] = True
    a = dfs(1)
    b = n-a
    visited[1] = False
    answer = min(answer, abs(a-b))

    return answer


def solution(n, wires):
    return min([get_diff(n, wires) for wires in list(combinations(wires, n-2))])