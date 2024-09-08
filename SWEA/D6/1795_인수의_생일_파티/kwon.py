import heapq  # 우선순위 큐 구현을 위함
from collections import defaultdict
INF = float('inf')

def dijkstra(graph, start):
    distances = {node: INF for node in graph}  # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
    
        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입
    
    return distances

# TC = int(input())

# for t in range(1, TC+1):
#     N, M, X = map(int, input().split())

#     graph = defaultdict(dict)
#     graph_rev = defaultdict(dict)
#     for _ in range(M):
#         x, y, c = map(int, input().split())
#         graph[x][y] = c
#         graph_rev[y][x] = c
    
#     # 순방향으로 인수의 집에서부터 노드까지 거리 구하기
#     # 인수 집에서 본인 집으로 돌아갈 때
#     distance = dijkstra(graph, X)

#     # 역방향으로 인수의 집에서 노드까지 거리 구하기
#     # 본인 집에서 인수 집으로 갈 때
#     distance_rev = dijkstra(graph_rev, X)

#     # print(distance, distance_rev)
#     ans = 0
#     for k in distance:
#         # 역방향(가는 길) + 순방향(돌아오는 길) -> 왕복 최소거리
#         ans = max(ans, distance[k]+distance_rev[k])

#     print(f"#{t} {ans}")





# import sys
# sys.stdin = open('input.txt', 'r')

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    line_li = [list(map(int, input().split())) for _ in range(M)]

    # 거리 확인할 배열 생성
    check_li = [[99999, 99999] for _ in range(N+1)]
    # print(check_li)

    # 기본거리로 수정
    check_li[0] = [0, 0]
    check_li[X] = [0, 0]
    for st, end, c in line_li:
        if end == X:
            check_li[st][0] = c
        if st == X:
            check_li[end][1] = c
    # print(check_li)

    # 경유지역누적거리 + 이번 거리 계산해서 min으로 갱신
    # temp_0 = []
    # temp_1 = []
    for i in range(1, N+1):
        temp_0 = [check_li[i][0]]
        temp_1 = [check_li[i][1]]
        for st, end, c in line_li:
            if end == i: # i로 오는 가중치 모두 저장
                cc = check_li[st][1]
                temp_1.append(c+check_li[st][1])
            if st == i: # i에서 나가는 가중치 모두 저장
                cc = check_li[end][0]
                temp_0.append(c+check_li[end][0])
        # i로 오는 최소값, i에서 가는 최소값
        check_li[i] = [min(temp_0), min(temp_1)]
        # print(check_li)

    print(f"#{tc} {max([a+b for a, b in check_li])}")