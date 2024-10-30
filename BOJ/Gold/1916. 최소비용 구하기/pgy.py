import sys
sys.stdin = open('input.txt', 'r')

import heapq

N = int(input().strip())
M = int(input().strip())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    arr[start].append((end, cost))
start_num, end_num = map(int, input().split())

INF = float('inf')
distances = [INF] * (N + 1)
distances[start_num] = 0 # 시작점이니까 비용 없음
queue = []
heapq.heappush(queue, (0, start_num))

while queue:
    current_dist, current_node = heapq.heappop(queue)

    if current_dist > distances[current_node]:
        continue

    for adjacent, weight in arr[current_node]:

        distance = current_dist + weight
        if distance < distances[adjacent]: # 더 짧은 경로를 찾으면 갱신
            distances[adjacent] = distance
            heapq.heappush(queue, (distance, adjacent))

print(distances[end])
