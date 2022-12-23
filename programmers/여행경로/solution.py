// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    n = len(tickets)
    answer = ['ZZZ']*(n+1)
    visited = set()
    
    def dfs(curr, route):
        nonlocal answer
        if len(route) == n+1:
            answer = min(answer, route)
            return
        
        for i, (start, depart) in enumerate(tickets):
            if start != curr or i in visited:
                continue
            visited.add(i)
            dfs(depart, route+[depart])
            visited.remove(i)
            
    dfs("ICN", ["ICN"])
    return answer