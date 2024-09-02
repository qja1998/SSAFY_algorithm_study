from collections import deque
 
def repair_road(road, N, value):
    queue = deque([(0, 0)])
    map_ = [[value] * N for _ in range(N)]
    map_[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in move:
            nx, ny = dx + x, dy + y
            if 0 <= nx < N and 0 <= ny < N:
                if map_[x][y] + road[nx][ny] < map_[nx][ny]:
                    map_[nx][ny] = map_[x][y] + road[nx][ny]
                    queue.append((nx, ny))
 
    return map_[N-1][N-1]
 
 
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
 
T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
    road = [list(map(int, input().rstrip())) for _ in range(N)]
    value = 0
    for k in range(N):
        value += sum(road[k])
    result = repair_road(road, N, value)
    print(f'#{test_case} {result}')