// [문제 링크]: https://www.acmicpc.net/problem/1717

n, m = map(int, input().split())
​
arr = [i for i in range(n+1)]
​
def find(a):
    if a == arr[a]:
        return a
    arr[a] = find(arr[a])
    return arr[a]
​
def is_union(a, b):
    return find(a) == find(b)
​
​
for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        arr[find(b)] = find(a)
    if c == 1:
        print("YES" if is_union(a, b) else "NO")