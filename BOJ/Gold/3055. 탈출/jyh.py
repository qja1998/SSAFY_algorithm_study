from collections import deque

# 입력 받기
R, C = map(int, input().split())
forest = [list(input().strip()) for _ in range(R)]

# 방향 벡터 (상, 하, 좌, 우)
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우

# 물과 고슴도치의 위치를 저장할 큐
water_queue = deque()
hedgehog_queue = deque()

# 방문 여부를 저장할 배열
water_time = [[-1] * C for _ in range(R)]  # 물이 차는 시간
hedgehog_time = [[-1] * C for _ in range(R)]  # 고슴도치가 이동한 시간

# 비버 굴 위치
beaver_r, beaver_c = -1, -1

# 초기 위치 설정
for i in range(R):
    for j in range(C):
        if forest[i][j] == 'S':  # 고슴도치의 초기 위치
            hedgehog_queue.append((i, j))
            hedgehog_time[i][j] = 0
        elif forest[i][j] == '*':  # 물의 초기 위치
            water_queue.append((i, j))
            water_time[i][j] = 0
        elif forest[i][j] == 'D':  # 비버의 굴 위치
            beaver_r, beaver_c = i, j

# 물이 퍼지는 BFS
while water_queue:
    x, y = water_queue.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            if forest[nx][ny] == '.' and water_time[nx][ny] == -1:
                water_time[nx][ny] = water_time[x][y] + 1
                water_queue.append((nx, ny))

# 고슴도치 이동 BFS
while hedgehog_queue:
    x, y = hedgehog_queue.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C:
            # 비버의 굴에 도착한 경우
            if forest[nx][ny] == 'D':
                print(hedgehog_time[x][y] + 1)
                exit()
            # 빈 칸으로 이동할 수 있는지 확인 (물보다 먼저 도착할 수 있어야 함)
            if forest[nx][ny] == '.' and hedgehog_time[nx][ny] == -1:
                # 물이 퍼지지 않았거나, 고슴도치가 더 빨리 도착할 수 있는 경우
                if water_time[nx][ny] == -1 or hedgehog_time[x][y] + 1 < water_time[nx][ny]:
                    hedgehog_time[nx][ny] = hedgehog_time[x][y] + 1
                    hedgehog_queue.append((nx, ny))

# 비버 굴에 도착하지 못한 경우
print("KAKTUS")

