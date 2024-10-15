from collections import defaultdict, deque
from itertools import combinations
from copy import deepcopy

# def show_map(enermy):
#     map_mat = [[0]*M for _ in range(N)]
#     for y in range(N):
#         for x in range(M):
#             if (x, y) in enermy:
#                 map_mat[y][x] = 1
#     return map_mat

dxy = [[-1, 0], [0, -1], [1, 0]]

N, M, D = map(int, input().split())

enermy = []

enermy_n = 0
for y in range(N):
    for x, value in enumerate(map(int, input().split())):
        if value == 0:
            continue
        enermy.append((x, y))
        enermy_n += 1

def shot(archer, enermy):
    q = deque([[archer, 0]])
    visited = [archer]

    while q:
        (c_x, c_y), cnt = q.popleft()

        if cnt > D:
            continue
        if (c_x, c_y) in enermy:
            return c_x, c_y
        for dx, dy in dxy:
            nx, ny = c_x + dx, c_y + dy
            
            if not(0 <= nx < M and 0 <= ny < N):
                continue

            q.append([(nx, ny), cnt+1])
            visited.append((nx, ny))
        
    return False

def step(archers, enermy, enermy_n):
    kill_cnt = 0
    while enermy_n > 0:
        shoted_enermy = set()
        for archer in archers:
            shoted_pos = shot(archer, enermy)
            if not shoted_pos:
                continue
            shoted_enermy.add(shoted_pos)
    
        for pos in list(shoted_enermy):
            enermy.remove(pos)
            enermy_n -= 1
            kill_cnt += 1
        
        new_enermy = []
        for i, (x, y) in enumerate(enermy):
            if y + 1 >= N:
                enermy_n -= 1
                continue
            new_enermy.append((x, y+1))
        
        enermy = new_enermy

    return kill_cnt
            
max_enermy = 0

for archers in combinations(range(M), 3):
    archers = list(zip(archers, [N]*M))
    max_enermy = max(max_enermy, step(deepcopy(archers), deepcopy(enermy), enermy_n))

print(max_enermy)