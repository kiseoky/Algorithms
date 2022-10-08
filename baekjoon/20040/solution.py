// [문제 링크]: https://www.acmicpc.net/problem/20040

import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
​
n, m = map(int, input().split())
parent = [i for i in range(n)]
answer = 0
​
def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]
​
for i in range(m):
    a, b = map(int, input().split())
​
    x, y = find(a), find(b)
    if x == y:
        answer = i+1
        break
    parent[x] = y
​
print(answer)
​
​
​