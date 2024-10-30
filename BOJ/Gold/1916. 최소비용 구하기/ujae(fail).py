from collections import deque

# 도시의 개수
N = int(input())
# 버스의 개수
M = int(input())
# 버스의 출발 도시 번호, 도착지의 도시 번호, 버스 비용
bus_info = [list(map(int, input().split())) for _ in range(M)]
# 출발 도시 번호, 도착 도시 번호
problem = list(map(int, input().split()))
bus_list = [[] for _ in range(N+1)]

for start, end, cost in bus_info:
    bus_list[start].append((end, cost))

result = float("inf")
def bfs(now_point, total_cost):
    global result
    queue = deque([(now_point, total_cost)])

    while queue:
        start_dot, cost = queue.popleft()
        if len(bus_list[start_dot]) > 1:
            for values in bus_list[start_dot]:
                if values[0] == problem[1]:
                    result = min(result, cost+values[1])
                else:
                    queue.append((values[0], cost+values[1]))

bfs(problem[0], 0)

print(result)
