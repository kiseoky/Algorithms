# a b면, b가 작은 순으로 연산
n = int(input())
m = []
for _ in range(n):
    a, b = map(int, input().split())
    m.append((a, b))


def find(num, arr):
    if arr[num] != num:
        arr[num] = find(arr[num], arr)
        return arr[num]
    return num


def union(p, c, arr):
    arr[find(c, arr)] = find(p, arr)


arr1 = [i for i in range(n)]
arr2 = [i for i in range(n)]

sorted_idx = sorted([i for i in range(n - 1)], key=lambda i: m[1:][i][1])

answer = 0
for idx in sorted_idx:
    answer += m[find(idx,arr1)][0] * m[find(idx,arr1)][1] * m[idx + 1][1]
    print(m[find(idx,arr1)][0], m[find(idx,arr1)][1], m[idx + 1][1], m[find(idx,arr1)][0] * m[find(idx,arr1)][1] * m[idx + 1][1])
    union(idx, idx + 1)
    m[idx] = (m[find(idx)][0], m[idx + 1][1])
    m[idx + 1] = (m[find(idx)][0], m[idx + 1][1])
    print(m[idx][0], m[idx][1], m[idx + 1][1], answer)

print(answer)
