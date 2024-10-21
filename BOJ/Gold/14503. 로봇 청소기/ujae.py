# def cleaning(y, x, path, count):
#     room_status[y][x] = 2
#     if count == 4:
#         dy = move[(path - 2) % 4][0]
#         dx = move[(path - 2) % 4][1]
#         ny = y + dy
#         nx = x + dx
#         if room_status[ny][nx] == 1:
#             return
#         else:
#             cleaning(ny, nx, path, 0)
#     dy = move[path][0]
#     dx = move[path][1]
#     ny = dy + y
#     nx = dx + x
#     if 0 <= ny < N and 0 <= nx < M:
#         if room_status[ny][nx] == 0:
#             cleaning(ny, nx, path, 0)
#         else:
#             cleaning(y, x, (path - 1) % 4, count + 1)


def cleaning2(y, x, path):
    # 현재 칸을 2로 바꿈 ( 2 : 청소 완료 )
    room_status[y][x] = 2
    pan = 0
    # 주변 4칸을 탐색
    for dy, dx in move:
        ny = dy + y
        nx = dx + x
        # 한 칸이라도 청소가 안되어 있다면
        if room_status[ny][nx] == 0:
            pan = 1
            break
    # 청소가 다 되었으면
    if pan == 0:
        # 방향 유지하고 뒤로 이동
        dy = move[(path - 2) % 4][0]
        dx = move[(path - 2) % 4][1]
        ny = dy + y
        nx = dx + x
        # 범위 안이라면
        if 0 <= ny < N and 0 <= nx < M:
            # 범위 안에 있더라도 벽이면 종료
            if room_status[ny][nx] == 1:
                return
            # 벽이 아니라면 이동
            else:
                cleaning2(ny, nx, path)
    else:
        path = (path - 1) % 4
        dy = move[path][0]
        dx = move[path][1]
        ny = dy + y
        nx = dx + x
        if room_status[ny][nx] == 0:
            cleaning2(ny, nx, path)
        else:
            cleaning2(y, x, path)


def see_move():
    now_shape = room_status
    return now_shape


move = ((-1, 0), (0, 1), (1, 0), (0, -1))

# N : y좌표, M : x좌표
N, M = list(map(int, input().split()))

# d값 : 0-북쪽, 1-동쪽, 2-남쪽, 3-서쪽
r, c, d = list(map(int, input().split()))

# 0 : 청소되지 않은 빈 칸, 1 : 벽 칸, 제일 가에쪽은 전부 다 벽(+ 가에쪽으로부터 1칸 이상이 벽임, 1칸일수도 그 이상일수도)
room_status = [list(map(int, input().split())) for _ in range(N)]

# 청소기 작동 방식
# 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
# 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
#   2.1 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
#   2.2 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
# 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
#   3.1 반시계 방향으로 90도 회전한다.
#   3.2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
#   3.3 1번으로 돌아간다.
# cleaning(r, c, d, 0)

cleaning2(r, c, d)

result = 0
for y1 in range(N):
    for x1 in range(M):
        if room_status[y1][x1] == 2:
            result += 1

print(result)
