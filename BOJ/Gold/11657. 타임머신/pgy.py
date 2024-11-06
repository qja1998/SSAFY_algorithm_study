import sys
sys.stdin = open('input.txt', 'r')

# 최단거리 - 벨만포드

N, M = map(int, input().split())
arr = []
INF = float('inf')
distance = [INF] * (N+1)

for i in range(M):
    start, end, time = map(int, input().split())
    arr.append((start, end, time))

distance[1] = 0 # 1번 노드는 0으로 초기화

for _ in range(N-1): # 노드가 N개이면 N-1번만 보면 다 볼 수 있음
    for start, end, time in arr:
        if distance[start] != INF and distance[end] > distance[start] + time: # 시작점이 무한대가 아니고,
            distance[end] = distance[start] + time # 새롭게 들어오는 시작점의 노드 + time 보다 더 작은 경우에 갱신

# 음수 사이클 확인
flag = False
for start, end, time in arr:
    if distance[start] != INF and distance[end] > distance[start] + time:
        flag = True

if not flag: # 음수 사이클이 아니라면
    for i in range(2, N+1): # 2번 노드가는 time 부터 출력
        if distance[i] != INF:
            print(distance[i])
        else:  # 그런데 아직도 INF 라면, 해당 노드엔 도달하지 못했다는 뜻이므로 -1 출력
            print(-1)

else:
    print(-1)

'''
import heapq

# 1. 순간이동 => -1 출력 후 아예 끝
# 2. 경로 없는 경우 => 해당 도시에 대해서만 -1 출력
# 3. N번 도시까지 가고 끝 => 도시별로 최소 시간 출력
# 최단 경로니까 다익스트라 => heapq 사용

def bfs(start):
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        cnode, ctime = heapq.heappop(queue)

        for end, time in arr[cnode]:
            time_sum = ctime + time
            if time_sum == 0:
                return -1
            if not end:
                time_arr[end] = -1
            if time_sum < time_arr[end]:
                time_arr[end] = time_sum
                heapq.heappush(queue, (time_sum, cnode + 1))

N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

min_time = float('inf')
time_arr = [min_time] * (N + 1)
time_arr[a] = 0
bfs(a)
for i in range(1, len(time_arr)):
    print(time_arr[i])
'''