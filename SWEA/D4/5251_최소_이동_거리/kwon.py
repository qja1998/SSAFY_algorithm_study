from collections import defaultdict
import heapq

INF = float('inf')

TC = int(input())

def dijkstra(graph, start):
    distances = [INF] * (N+1)
    distances[start] = 0

    visited = set()
    min_heap = []
    heapq.heapify(min_heap)
    heapq.heappush(min_heap, [0, start])

    while min_heap:
        w, v = heapq.heappop(min_heap)

        if v in visited:
            continue

        visited.add(v)
        
        for nv, nw in graph[v].items():
            n_dist = w + nw
            if n_dist < distances[nv]:
                distances[nv] = n_dist
                heapq.heappush(min_heap, [distances[nv], nv])
    return distances

for t in range(1, TC+1):
    N, E = map(int, input().split())

    graph = defaultdict(dict)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s][e] = w
    
    dist = dijkstra(graph, 0)

    print(f"#{t} {dist[N]}")