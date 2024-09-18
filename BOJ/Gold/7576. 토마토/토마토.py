from collections import deque
m, n = map(int, input().split())

boxes = []
q = deque()

for y in range(n):
    row = list(map(int, input().split()))
    boxes.append(row)
    for x in range(m):
        if row[x] == 1:
            # 위치, 시간
            q.append((x, y, 0))
    
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS
while q:
    x, y, cnt = q.popleft()

    # 사방탐색
    for i in range(4):
        x_tmp, y_tmp = x + dx[i], y + dy[i]
        if 0 <= x_tmp < m and 0 <= y_tmp < n and boxes[y_tmp][x_tmp] != -1:
            if boxes[y_tmp][x_tmp] == 0:
                boxes[y_tmp][x_tmp] = 1
                # 익힐 수 있을 경우 익히고, 시간 + 1
                q.append((x_tmp, y_tmp, cnt + 1))

for row in boxes:
    # 안익은 토마토 있을 때
    if 0 in row:
        cnt = -1
        break
print(cnt)