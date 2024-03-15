# 크루스칼 + 가장 큰 비용 제거(마을 분할)
# 틀린 부분
#   - union 연산 시 부모끼리 할당해야함.
#     - parent[find(b)] = find(a) << 어차피 find 연산 시 자손들은 모두 부모 값으로 치환됨
#     + union 연산 시 a, b 크기에 따라 할당 로직이 필요한가?
#       - 이 문제에선 해당 로직이 없어서 정답 처리됨. 시간은 200ms 더 걸림
#       - 틀리진 않지만 추가적인 연산이 필요할 수 있음 정도로 예상됨. 문제 풀면서 데이터를 쌓아보자.
import sys

n, m = map(int, sys.stdin.readline().strip().split())

roads = []

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    roads.append((a, b, c))

roads.sort(key=lambda x: x[2])

parent = [i for i in range(n + 1)]


def find(num):
    if parent[num] != num:
        parent[num] = find(parent[num])
    return parent[num]


def union(a, b):
    p_a, p_b = find(a), find(b)
    parent[p_b] = find(p_a)


answer = 0
max_cost = 0

for a, b, cost in roads:
    if find(a) == find(b):
        continue
    union(a, b)
    answer += cost
    max_cost = max(cost, max_cost)

print(answer - max_cost)
