'''
https://www.acmicpc.net/problem/1697
수빈이가 있는 지점에서 걸어갈지 순간이동을 할 지 선택
이동하며 curr_sec 증가
동생이 있는 지점에 도착할 때까지 반복
도착한 경우 min_sec 갱신
만약 현재 curr_sec이 min_sec보다 큰 경우 가지치기

-------
dfs로 했다가 자멸하고 bfs로 8ight톤 트럭 돌림

'''

from collections import deque

start_point, end_point = map(int, input().split())
# print(N, M)

visited = [float('inf')] * 100001   # 방문 리스트

def search(pos, spend_t, v):
    deq = deque([(pos, spend_t)])

    while deq:
        # (이동 위치) , 현재 소요 시간
        c_pos, c_time = deq.popleft()

        # 도착 지점인 경우
        if c_pos == end_point:
            visited[c_pos] = min(v[c_pos], c_time)
            return

        # 방문 체크
        if v[c_pos] <= c_time: continue
        v[c_pos] = c_time

        # 전진
        if 0 <= c_pos +1 <= 100000:
            deq.append((c_pos+1, c_time+1))

        # 후진
        if 0 <= c_pos - 1 <= 100000:
            deq.append((c_pos - 1, c_time + 1))

        # 텔포
        if 0 <= c_pos * 2 <= 100000:
            deq.append((c_pos * 2, c_time + 1))

    return


# 현재 위치, 시간
search(start_point, 0, visited)

print(visited[end_point])


# from collections import deque
#
# N, M = map(int, input().split())
# # print(N, M)
#
# visited = [float('inf')] * 100001   # 방문 리스트
#
# def search(pos, spend_t, visited):
#     visited[pos] = spend_t
#
#     deq = deque([((pos -1, pos +1, pos *2), spend_t +1)])
#
#     while deq:
#         # (이동 위치) , 현재 소요 시간
#         current_points, current_t = deq.popleft()
#         tmp_list = list()
#
#         # 각 이동한 지점에 대해서
#         for point in current_points:
#             # 이동한 지점이 도착 지점이라면
#             # 이전에 저장되어 있던 값과 비교 => 더 짧은 시간이 소요됐다면 갱신
#             if point == M:
#                 visited[point] = min(visited[point], current_t)
#                 return
#
#             # 이동한 지점이 범위를 벗어났다면 다음 지점으로 넘어감
#             if not (0 <= point <= 100000): continue
#
#             # 이전에 이미 방문한 지점
#             if visited[point] > current_t: continue
#
#             visited[point] = min(visited[point], current_t) # 최소 소요시간 비교 후 갱신
#
#             tmp_list.append(point)