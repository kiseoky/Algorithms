# unmerge 하나씩 하다 틀림.
# 앞에서부터 unmerge 하면 parent[(뒷)] = (앞)인 경우 예외 케이스. 처리할 item을 배열에 담고 한번에 처리해서 해결
def solution(commands):
    answer = []
    table = [['EMPTY'] * 51 for _ in range(51)]
    parent = [[(i, j) for j in range(51)] for i in range(51)]

    def find(r, c):
        if parent[r][c] != (r, c):
            parent[r][c] = find(*parent[r][c])
        return parent[r][c]

    def union(r1, c1, r2, c2):
        pr1, pc1 = find(r1, c1)
        pr2, pc2 = find(r2, c2)
        if table[pr1][pc1] == 'EMPTY' and table[pr2][pc2] != 'EMPTY':
            pr1, pc1, pr2, pc2 = pr2, pc2, pr1, pc1
        parent[pr2][pc2] = (pr1, pc1)

    def un_union(r, c):
        pr, pc = find(r, c)
        table[r][c] = table[pr][pc]
        clear_list = []
        for i in range(1, 51):
            for j in range(1, 51):
                pi, pj = find(i, j)
                if (pi, pj) == (pr, pc):
                    clear_list.append((i, j))

        for y, x in clear_list:
            parent[y][x] = (y, x)
            if (y, x) != (r, c):
                table[y][x] = 'EMPTY'

    def update(r, c, value):
        pr, pc = find(r, c)
        table[pr][pc] = value

    def update_value(value1, value2):
        for i in range(1, 51):
            for j in range(1, 51):
                if table[i][j] == value1:
                    table[i][j] = value2

    for command in commands:
        if command.startswith("UPDATE"):
            contents = command.split()

            if len(contents) == 4:
                _, r, c, value = contents
                update(int(r), int(c), value)
            else:
                _, value1, value2 = contents
                update_value(value1, value2)

        if command.startswith("MERGE"):
            r1, c1, r2, c2 = map(int, command.split()[1:])
            union(r1, c1, r2, c2)
        if command.startswith("UNMERGE"):
            r, c = map(int, command.split()[1:])
            un_union(r, c)
        if command.startswith("PRINT"):
            r, c = map(int, command.split()[1:])
            pr, pc = find(r, c)
            answer.append(table[pr][pc])

    return answer

# print(solution(["UPDATE 1 2 menu", "MERGE 1 1 1 2", "UNMERGE 1 2", "PRINT 1 1", "PRINT 1 2"]))
# 2차원 배열
# 1. O(1)
# 2. O(N^2)
# 3. O(1) - union find
# 4. un union - 선택한 cell과 같은 parent면 초기화
# 5. O(1)