from collections import defaultdict
import heapq

INF = float('inf')
N = int(input())
M = int(input())

def heapfy_list():
    empty = []
    heapq.heapify(empty)
    return empty

station_graph = defaultdict(list)

for _ in range(M):
    s, e, cost = map(int, input().split())
    station_graph[s].append((e, cost))

start, dest = map(int, input().split())


def dijkstra(start, dest):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q, (0, start)) # 우선순위, 값 형태로 들어간다.
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 우선순위가 가장 낮은 값(가장 작은 거리)이 나온다.

        if distance[now] < dist: # 이미 입력되어있는 값이 현재노드까지의 거리보다 작다면 이미 방문한 노드이다.
            continue               # 따라서 다음으로 넘어간다.

        for station in station_graph[now]:     # 연결된 모든 노드 탐색
            if dist + station[1] < distance[station[0]]: # 기존에 입력되어있는 값보다 크다면
                distance[station[0]] = dist + station[1]   #
                heapq.heappush(q, (dist+station[1], station[0]))

                print(dest)

    return distance[dest]

print(dijkstra(start, dest))