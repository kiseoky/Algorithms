// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    sizes = sorted(sizes, reverse=True)
    
    maxW, maxH = sizes[0]
    for w, h in sizes[1:]:
        m1 = max(w, maxW) * max(h, maxH)
        m2 = max(h, maxW) * max(w, maxH)
        if m1 <= m2:
            maxW, maxH = max(w, maxW), max(h, maxH)
        else:
            maxW, maxH = max(h, maxW), max(w, maxH)
    return maxW*maxH



### 1
# 1) 가로 max, 세로 max를 구한다. with index
# 2) 가로 max 항목을 switch 후 값 비교
# 3) 세로 max 항목을 switch 후 값 비교
# 4) 두 값 다 변동이 업을 때까지 반복

### 2
# 모든 경우의 수 돌리기
# 2^10000

### 3
# 가로길이 기준 내림차순 sort
# 최대한 안바뀌는 쪽으로 돌려본 후 넘어간다.