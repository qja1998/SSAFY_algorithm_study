from collections import deque

test_case = int(input())

# 우하 방향으로만 가면 됨
dxy = [(0, 1), (1, 0)]

for t in range(test_case):
    n = int(input())
    # [구멍, 이 위치에서의 최소 총 공사시간]
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
            # (지금까지의 총 공사시간 + 현재 위치의 필요 시간)이 더 작을 경우 갱신
            road_map[ny][nx][1] = road_map[y][x][1] + road_map[ny][nx][0]
            q.append((ny, nx))

    # 최우하단 위치의 총 공사시간 출력
    print(f"#{t + 1} {road_map[n - 1][n - 1][1]}")