from collections import deque
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def down_stair(stair_q1, stair_q2):
    stair_q1 = deque((sorted(stair_q1)))
    stair_q2 = deque((sorted(stair_q2)))
    waiting1 = deque()
    waiting2 = deque()
    
    time = 0
    while stair_q1 or stair_q2 or waiting1 or waiting2:

        # 1번 계단으로 접근
        i = 0
        while i < len(stair_q1):
            # 도착하면 계단에 넣기
            if stair_q1[i] == -1:
                waiting1.append(stair1)
                stair_q1.popleft()
                continue
            stair_q1[i] -= 1
            i += 1
        # 2번 계단으로 접근
        
        i = 0
        while i < len(stair_q2):
            # 도착하면 계단에 넣기
            if stair_q2[i] == -1:
                waiting2.append(stair2)
                stair_q2.popleft()
                continue
            stair_q2[i] -= 1
            i += 1

        # 1번 계단에서 내려감
        for i in range(3):
            # 앞 3명만 내려갈 수 있음
            if i > len(waiting1)-1:
                break
            if waiting1[i] == 0:
                continue
            waiting1[i] -= 1
        for _ in range(3):
            if not waiting1:
                break
            if waiting1[0] == 0:
                waiting1.popleft()

        # 2번 계단에서 내려감
        for i in range(3):
            # 앞 3명만 내려갈 수 있음
            if i > len(waiting2)-1:
                break
            if waiting2[i] == 0:
                waiting2.popleft()
                continue
            waiting2[i] -= 1

        for _ in range(3):
            if not waiting2:
                break
            if waiting2[0] == 0:
                waiting2.popleft()
        
        time += 1
    return time

def search_stair(dist_list1, dist_list2, stair_q1=[], stair_q2=[]):
    global min_time
    if len(stair_q1)+len(stair_q2) == n_people:
        min_time = min(min_time, down_stair(stair_q1, stair_q2))
        return
    
    for i in range(len(dist_list1)):
        # 1번 계단 선택
        search_stair(dist_list1[i+1:], dist_list2[i+1:], stair_q1+[dist_list1[i]], stair_q2)
        # 2번 계단 선택
        search_stair(dist_list1[i+1:], dist_list2[i+1:], stair_q1, stair_q2+[dist_list2[i]])


# 주어진 입력 받기
T = int(input())
for t in range(1, T+1):
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
        dist = []
        for stair_pos in stairs:
            dist.append(abs(person_pos[0] - stair_pos[0]) + abs(person_pos[1] - stair_pos[1]))
        dist_list.append(dist)
    
    stair1, stair2 = stairs.values()
    dist_list1, dist_list2 = zip(*dist_list)
    n_people = len(persons)

    min_time = float('inf')
    search_stair(dist_list1, dist_list2)

    print(f"#{t+1} {min_time}")