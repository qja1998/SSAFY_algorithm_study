N, M = list(map(int, input().split()))
bus_info = [list(map(int, input().split())) for _ in range(M)]

graph = [[] for _ in range(N + 1)]

for A, B, C in bus_info:
    graph[A].append((B, C))

INF = float('inf')
visited = [INF] * (N + 1)


def bellman_ford(start):
    visited[start] = 0

    for _ in range(N - 1):
        for A, B, C in bus_info:
            if visited[A] != INF and visited[A] + C < visited[B]:
                visited[B] = visited[A] + C

    for A, B, C in bus_info:
        if visited[A] != INF and visited[A] + C < visited[B]:
            print(-1)
            exit()

bellman_ford(1)

for i in range(2, N + 1):
    if visited[i] == INF:
        print(-1) 
    else:
        print(visited[i])