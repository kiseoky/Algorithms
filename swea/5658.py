t = int(input())
for tc in range(1, t + 1):
    n, k = map(int, input().split())
    nums_set = set()
    a = n // 4
    s = input()


    def get_c(idx):
        if idx >= n:
            return s[idx-n]
        return s[idx]


    def get_num(idx):
        ret = ''
        for i in range(idx, idx + a):
            ret += get_c(i)
        return ret


    def to_ten(s):
        p = '0123456789ABCDEF'
        n = len(s)
        ret = 0
        for i in range(len(s)):
            ret += p.index(s[i]) * pow(16, n - i - 1)
        return ret


    for i in range(n):
        nums_set.add(get_num(i))

    print(f"#{tc} {sorted([to_ten(num) for num in nums_set], reverse=True)[k - 1]}")
