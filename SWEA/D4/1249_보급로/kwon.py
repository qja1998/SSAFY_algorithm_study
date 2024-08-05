from collections import deque

test_case = int(input())

dxy = [(0, 1), (1, 0)]

for t in range(test_case):
    n = int(input())
    road_map = [[[int(s), 2147483647] for s in input()] for i in range(n)]

    q = deque([(0, 0)])
    road_map[0][0][1] = 0

    while q:
        y, x = q.popleft()
        for dy, dx in dxy:
            ny, nx = y + dy, x + dx

            # 범위 확인
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if road_map[ny][nx][1] < road_map[y][x][1] + road_map[ny][nx][0]:
                continue
            road_map[ny][nx][1] = road_map[y][x][1] + road_map[ny][nx][0]
            q.append((ny, nx))

    print(f"#{t + 1} {road_map[n - 1][n - 1][1]}")