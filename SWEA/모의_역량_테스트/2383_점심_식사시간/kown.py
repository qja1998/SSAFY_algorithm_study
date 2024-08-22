import sys
sys.stdin = open("sample_input.txt", "r")

from collections import defaultdict
from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def search_stair(stair_q1, stair_q2, dist_list, time=1):
    # 동시에 들어오면 다른 계단에서 먼 쪽이 들어가도록
    while stair_q1 or stair_q2 or dist_list:
        # 도달할 시간이 되면 들어가도록

        # 한 사람이 동시에 두 계산에 도달하는 경우는?
        
    search_stair()


# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms_matrix = [list(map(int, input().split())) for _ in range(N)]

    persons = []
    stairs = {}

    for y in range(N):
        for x in range(N):
            if rooms_matrix[y][x] == 1:
                persons.append((y, x))
            if rooms_matrix[y][x] > 1:
                stairs[(y, x)] = rooms_matrix[y][x]

    dist_list = []
    for person_pos in persons:
        for stair_pos in stairs:
            dist = abs(person_pos[0] - stair_pos[0]) + abs(person_pos[1] - stair_pos[1])
            dist_list.append(dist)
    
    dist_list1, dist_list2 = zip(*dist_list)

    stair_q1 = deque()
    stair_q2 = deque()