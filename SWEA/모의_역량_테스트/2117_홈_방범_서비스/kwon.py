# 운용비용 = k **2 + (k - 1) ** 2
from collections import defaultdict, deque
test_case = int(input())

import copy
def show_map(visited):
    tmp = copy.deepcopy(houses_map)
    for y, x in visited:
        tmp[y][x] += 2

    return tmp

dyx = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def cnt_diamonds(y, x):
    global max_house
    visited = defaultdict(bool)
    house_cnt = 0
    q = deque([(y, x, 1)])
    visited[(y, x)] = True
    while q:
        y, x, cnt = q.popleft()

        if houses[(y, x)]:
            house_cnt += 1

        if (cnt ** 2 + (cnt - 1) ** 2) <= (m * house_cnt):
            max_house = max(max_house, house_cnt)

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if not (0 <= nx < n) or not (0 <= ny < n):
                continue
            if visited[(ny, nx)]:
                continue
            visited[(ny, nx)] = True
            q.append((ny, nx, cnt + 1))

for t in range(test_case):
    n, m = map(int, input().split())

    houses_map = [list(map(int, input().split())) for _ in range(n)]

    houses = defaultdict(bool)
    for i in range(n):
        for j in range(n):
            if houses_map[i][j] == 1:
                houses[(i, j)] = True


    max_house = 0
    for i in range(n):
        for j in range(n):
            cnt_diamonds(j, i)

    print(f'#{t + 1} {max_house}')