n, s = map(int, input().split())

arr = list(map(int, input().split()))

summed = [0]

for i in range(n):
    summed.append(arr[i] + summed[i])

l, r = 0, 1
ans = 10e9
while l < r <= n:
    val = summed[r] - summed[l]
    if val >= s:
        ans = min(ans, r - l)
        l += 1
    if val < s:
        r += 1

if ans == 10e9:
    ans = 0

print(ans)
