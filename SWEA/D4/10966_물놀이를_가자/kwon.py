TC = int(input())

from collections import deque

dyx = [[0, 1], [1, 0], [0, -1], [-1, 0]]

for t in range(1, TC+1):
    N, M = map(int, input().split())

    distances = [[-1]*M for _ in range(N)]
    water_q = deque()

    for y in range(N):
        row = input()
        for x in range(M):
            if row[x] == 'W':
                water_q.append((y, x))
                distances[y][x] = 0

    # 모두 물이거나 땅
    if len(water_q) == 0 or len(water_q) == N*M:
        print(f"#{t} 0")
        continue

    
    while water_q:
        y, x = water_q.popleft()

        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            # 범위 벗어날 때
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            
            if distances[ny][nx] != -1:
                continue

            # 거리 갱신
            distances[ny][nx] = distances[y][x] + 1
            water_q.append((ny, nx))


    result = 0
    for y in range(N):
        for x in range(M):
            result += distances[y][x]
    print(f"#{t} {result}")
