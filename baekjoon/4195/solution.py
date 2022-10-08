// [문제 링크]: https://www.acmicpc.net/problem/4195

from collections import defaultdict
​
t = int(input())
​
for _ in range(t):
    f = int(input())
    users = {}
    cnt = defaultdict(lambda: 1)
​
    def find(a):
        if a not in users:
            users[a] = a
​
        if a == users[a]:
            return a
        users[a] = find(users[a])
        return users[a]
​
    for _ in range(f):
        a, b = input().split()
        x, y = find(a), find(b)
        if x != y:
            x, y = find(a), find(b)
            users[x] = y
            cnt[y] += cnt[x]
        print(cnt[y])