R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
up, down = [i for i in range(R) if A[i][0] == -1]

for _ in range(T):
    # 확산
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    cnt_arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A[i][j] != 0 and A[i][j] != -1:
                cnt = 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                        cnt_arr[nx][ny] += A[i][j] // 5
                        cnt += A[i][j] // 5
                A[i][j] -= cnt

    for i in range(R):
        for j in range(C):
            A[i][j] += cnt_arr[i][j]

    # 위쪽 청정기
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = up, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        A[x][y], before = before, A[x][y]
        x = nx
        y = ny
    # 아래쪽 청정기
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = down, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        A[x][y], before = before, A[x][y]
        x = nx
        y = ny

# result = 0
# for i in range(R):
#     for j in range(C):
#         if A[i][j] > 0:
#             result += A[i][j]

result = sum(map(lambda x: sum(i for i in x if i > 0), A))

print(result)