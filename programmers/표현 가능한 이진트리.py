# 어거지로 푼 느낌이다.
# 기본적으로 root를 확인하고 left, right 나누어 dfs 탐색, root가 0이면 return False
# edge 테스트 케이스를 하나 만들어두고 통과하도록 만듦.
# - 1111
#   - 짝수인 경우, 0을 홀수개만큼 붙여가면서 확인
#     - 0001111 일 때 정답.
#   - b 값이 모두 0인 경우 return True
#   - b 길이가 1이면 return True, but depth가 다른 leaf와 다르면 return False
import math


def solution(numbers):
    answer = []

    max_d = 0

    def b_tree_able(b, d):
        nonlocal max_d
        if d == 0:
            max_d = 0
        max_d = max(max_d, d)
        if len(b) == 1:
            return max_d == d
        if len(b) % 2 == 0:
            if d == 0:
                for i in range(1, len(b), 2):
                    if b_tree_able(('0' * i) + b, 0):
                        return True
                return False
            else:
                return False
        if b == '0' * len(b):
            max_d = max(max_d, math.log(len(b) + 1))
            return True
        m = len(b) // 2

        if b[m] == '0':
            return False

        return b_tree_able(b[:m], d + 1) and b_tree_able(b[m + 1:], d + 1)

    return [int(b_tree_able(bin(number)[2:], 0)) for number in numbers]
