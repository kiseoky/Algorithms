import sys

n = int(input())
min_a, min_b, min_c = 0, 0, 0
max_a, max_b, max_c = 0, 0, 0
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    min_a, min_b, min_c = min(min_a, min_b) + a, min(min_a, min_b, min_c) + b, min(min_b, min_c) + c
    max_a, max_b, max_c = max(max_a, max_b) + a, max(max_a, max_b, max_c) + b, max(max_b, max_c) + c

print(max(max_a, max_b, max_c), min([min_a, min_b, min_c]))
