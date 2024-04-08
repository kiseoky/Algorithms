import heapq


def solution(n, paths, gates, summits):
    answer = []
    gate_set = set(gates)
    summit_set = set(summits)
    dis = [10e7] * (n + 1)

    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    queue = []

    for gate in gates:
        queue.append((0, gate))
        dis[gate] = 0

    while queue:
        intensity, node = heapq.heappop(queue)
        if dis[node] < intensity:
            continue
        if node in summit_set:
            print(dis)
            return [node, intensity]

        for n_node, n_intensity in graph[node]:
            n_intensity = max(intensity, n_intensity)
            if dis[n_node] <= n_intensity:
                continue
            print(node, n_node, n_intensity)
            dis[n_node] = n_intensity
            heapq.heappush(queue, (dis[n_node], n_node))

    return answer

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]
))