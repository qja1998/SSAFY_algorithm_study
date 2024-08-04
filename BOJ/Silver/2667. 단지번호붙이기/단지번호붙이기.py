from collections import deque

n = int(input())

buildings = []
for _ in range(n):
    
    buildings.append([int(i) for i in input()])



# chk_map = [b[:] for b in buildings]

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def bfs(buildings, x, y):
    q = deque()
    q.append((x, y))
    buildings[y][x] = 0
    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1

        for i in range(4):
            x_tmp, y_tmp = x + dx[i], y + dy[i]
            if 0 <= x_tmp < n and 0 <= y_tmp < n:
                if buildings[y_tmp][x_tmp] != 0:
                    q.append((x_tmp, y_tmp))
                    buildings[y_tmp][x_tmp] = 0
    return cnt

results = []

for y in range(n):
    for x in range(n):
        if buildings[y][x] != 0:
            results.append(bfs(buildings, x, y))

print(len(results))

for r in sorted(results):
    print(r)