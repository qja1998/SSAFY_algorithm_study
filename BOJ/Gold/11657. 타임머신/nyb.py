'''
https://www.acmicpc.net/problem/11657

시작점이 지정되어 있는 문제
시작점을 기준으로 가장 비용이 적은 경로 찾기

음수 가중치가 있기 때문에

....
아니... 예제 2번 이해가 안 감
무한히 오래 전으로 되돌릴 수 있다면 -1 출력 => 음수 사이클이 있다면?
'''

from collections import defaultdict

CITY_N, BUS_N = map(int, input().split())
bus_dict = defaultdict(list)
min_distance = [float('inf')] * (CITY_N+1)   # 최단거리 저장 리스트 1부터 시작해야함
start_num = 1
min_distance[start_num] = 0 # 시작지점 거리 0으로 초기화

# 버스 노선 정보 값을 저장하는 딕셔너리
for _ in range(BUS_N):
    a = list(map(int, input().split()))
    bus_dict[a[0]].append((a[1], a[2]))

# print(bus_dict)

for _ in range(CITY_N-1):
    for start in bus_dict.keys():
        for stop, distance in bus_dict[start]:
            if min_distance[start] + distance < min_distance[stop]:
                min_distance[stop] = min_distance[start] + distance # 거리 최소값 갱신

# 음수 사이클 검출
for start in bus_dict.keys():
    for stop, distance in bus_dict[start]:
        if min_distance[start] + distance < min_distance[stop]: # 음수 사이클 존재
            print(-1)
            quit()

# 최단 거리 출력하며 만약 갱신이 안 된 곳이 있다면 갈 수 없는 곳이기 때문에 -1 출력
for i in range(2, CITY_N+1):
    if min_distance[i] == float('inf'):
        print(-1)
    else:
        print(min_distance[i])