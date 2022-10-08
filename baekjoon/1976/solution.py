// [문제 링크]: https://www.acmicpc.net/problem/1976

n = int(input())
m = int(input())
​
lines = [[0]*(n+1)]
for _ in range(n):
    lines.append([0]+list(map(int, input().split())))
​
plan = list(map(int, input().split()))
​
​
arr = [i for i in range(n+1)]
​
def find(a):
    if a == arr[a]:
        return a
    arr[a] = find(arr[a])
    return arr[a]
​
def is_union(plan):
    b = -1
    for a in plan:
        if b != -1 and find(a) != b:
            return "NO"
        b = find(a)
    return "YES"
​
for i in range(1, n+1):
    for j in range(1, n+1):
        if lines[i][j] == 1:
            arr[find(i)] = find(j)
​
print(is_union(plan))