INF = float('inf')

N, M = map(int, input().split())
M_edges = [tuple(map(int, input().split())) for _ in range(M)]
distance = [INF] * (N + 1)

def bellman_ford(start_node):
    distance[start_node] = 0
    for i in range(N):
        for j in range(M):
            current_node = M_edges[j][0]
            next_node = M_edges[j][1]
            edge_cost = M_edges[j][2]
            if distance[current_node] != INF and distance[next_node] > distance[current_node] + edge_cost:
                distance[next_node] = distance[current_node] + edge_cost
                if i == N - 1:
                    return True
    return False


negative_circulation = bellman_ford(1)

if negative_circulation:
    print(-1)
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])
