// [문제 링크]: https://www.acmicpc.net/problem/4195

import sys
input = sys.stdin.readline
t = int(input())
​
for _ in range(t):
    f = int(input())
    users = {}
    cnt = {}
​
    def find(a):
        if a == users[a]:
            return a
        users[a] = find(users[a])
        return users[a]
​
    for _ in range(f):
        a, b = map(str, input().split())
        if a not in users:
            users[a] = a
            cnt[a] = 1
        if b not in users:
            users[b] = b
            cnt[b] = 1
​
        x, y = find(a), find(b)
        if x != y:
            users[y] = x
            cnt[x] += cnt[y]
        print(cnt[find(a)])