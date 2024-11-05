from collections import defaultdict
N, M = map(int, input().split())

INF = float('inf')

bus_graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, input().split())
    bus_graph[a].append((b, c))

def bellman(start, graph):
    dist = [INF] * (N + 1)
    dist[start] = 0

    for _ in range(N-1):
        for c_node in graph:
            for n_node, cost in graph[c_node]:

                if dist[c_node] != INF and dist[n_node] > dist[c_node] + cost:
                    dist[n_node] = dist[c_node] + cost

    for c_node in graph:
        for n_node, cost in graph[c_node]:

            # 또 갱신되는 경우(음수 사이클)
            if dist[c_node] != INF and dist[n_node] > dist[c_node] + cost:
                return False

    return dist[2:]

result = bellman(1, bus_graph)
if result:
    for d in result:
        if d == INF:
            print(-1)
        else:
            print(d)
else:
    print(-1)