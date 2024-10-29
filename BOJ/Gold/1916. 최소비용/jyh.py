import heapq

def dijkstra(n, start, end, graph):
    # 최단 거리를 저장하는 배열 초기화
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    # 우선순위 큐 초기화
    queue = [(0, start)]

    while queue:
        # 현재 노드까지의 비용과 현재 노드
        current_cost, current_node = heapq.heappop(queue)

        # 현재 노드의 비용이 이미 기록된 비용보다 크다면 넘어감
        if distance[current_node] < current_cost:
            continue

        # 인접 노드들에 대해
        for adjacent, weight in graph[current_node]:
            cost = current_cost + weight
            # 현재 경로가 더 짧은 경우 업데이트
            if cost < distance[adjacent]:
                distance[adjacent] = cost
                heapq.heappush(queue, (cost, adjacent))

    return distance[end]

n = int(input())
m = int(input())

# 그래프 초기화
graph = [[] for _ in range(n + 1)]
for i in range(2, m + 2):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 시작 도시와 도착 도시
start, end = map(int, input().split())

# 다익스트라 알고리즘을 사용하여 최소 비용 계산
result = dijkstra(n, start, end, graph)
print(result)
