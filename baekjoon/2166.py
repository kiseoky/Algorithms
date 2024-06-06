n = int(input())
y = []
x = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x += [x[0]]
y += [y[0]]

result = 0
for i in range(n):
    result += x[i + 1] * y[i] - x[i] * y[i + 1]

print(round(abs(result) / 2, 1))
