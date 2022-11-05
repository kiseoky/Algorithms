// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def get_diff(word1, word2):
    n = len(word1)
    return sum([word1[i] != word2[i] for i in range(n)])

def solution(begin, target, words):
    queue = deque([(begin, 0)])
    visited = set()
    
    while queue:
        curr, cnt = queue.popleft()
        visited.add(curr)
        if curr == target:
            return cnt
        for word in words:
            if word not in visited and get_diff(curr, word) == 1:
                queue.append((word, cnt+1))
    return 0

