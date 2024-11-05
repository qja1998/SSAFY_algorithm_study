from collections import deque
from math import ceil

N, M, K = map(int, input().split())

mushrooms = [list(map(int, input().split())) for _ in range(N)]

mushroom_cnt = 0

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def search(start, mushrooms):
    q = deque([start])
    visited = [start]

    cnt = 1
    while q:
        # print(q)
        x, y = q.popleft()
        mushrooms[y][x] = -1

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            # print(nx, ny)
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if (nx, ny) in visited:
                continue
            if mushrooms[ny][nx] == 1:
                continue
            
            q.append((nx, ny))
            visited.append((nx, ny))
            cnt += 1
    return cnt

is_possible = True
for y in range(N):
    for x in range(N):
        if mushrooms[y][x] != 0:
            continue
        local_cnt = search((x, y), mushrooms)
        # for row in mushrooms:
            # print(row)
        # print(local_cnt)

        mushroom_cnt += ceil(local_cnt / K)
        if mushroom_cnt > M:
            is_possible = False
            break

    if not is_possible:
        break

if is_possible and mushroom_cnt != 0:
    print("POSSIBLE")
    print(M - mushroom_cnt)
else:
    print("IMPOSSIBLE")