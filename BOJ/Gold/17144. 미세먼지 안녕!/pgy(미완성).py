import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# 미세먼지 확산
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def dust(x, y):
    global time
    queue = deque()
    queue.append((x, y))
    while queue:
        cx, cy = queue.popleft()

        if time == T:
            return

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            if nx < 0 or nx >= R or ny < 0 or ny >= C: # 칸이 없으면 확산 X
                continue

            if arr[nx][ny] == -1: # 공기청정기가 인접하면 확산 X
                continue

            arr[nx][ny]
            queue.append((nx, ny))
            time += 1

# 공기청정기 작동 (위쪽 => 반시계방향)
def air_reverse(i, j):
    global time
    # === 작성해야 함 ===

# 공기청정기 작동 (아래쪽 => 시계방향)
def air(i, j):
    global time
    # === 작성해야 함 ===

flag = False
time = 0
res = 0
dust(0, 0)
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1 and flag == False: # flag로 공기청정기 위쪽
            air_reverse(i, j)
            flag = True
        elif arr[i][j] == -1 and flag == True: # 공기청정기 아래쪽 각각 함수 실행해주기
            air(i, j)

for i in range(R):
    for j in range(C):
        res += arr[i][j]
print(res)