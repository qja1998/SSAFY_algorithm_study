from collections import deque

move = ((0, -1), (-1, 0), (0, 1), (1, 0))


def one_second(num):
    for _ in range(num):
        dust_movement()
        wind_movement()

def dust_movement():
    global room_info
    room_info_copy = [[0]*C for _ in range(R)]
    for y_, x_ in air_purifier:
        room_info_copy[y_][x_] = -1

    queue = deque([])
    for y1 in range(R):
        for x1 in range(C):
            if room_info[y1][x1] != -1 and room_info[y1][x1] != 0:
                queue.append((y1, x1))

    while queue:
        now_y, now_x = queue.popleft()
        value = (room_info[now_y][now_x] // 5)
        count = 0
        for dy, dx in move:
            ny = now_y + dy
            nx = now_x + dx
            if 0 <= ny < R and 0 <= nx < C and room_info[ny][nx] != -1:
                room_info_copy[ny][nx] += value
                count += 1
        room_info_copy[now_y][now_x] += (room_info[now_y][now_x] - (count * value))

    room_info = [row[:] for row in room_info_copy]

def wind_movement():
    for i in range(len(up_list) - 1):
        room_info[up_list[i][0]][up_list[i][1]] = room_info[up_list[i + 1][0]][up_list[i + 1][1]]
    room_info[up_list[-1][0]][up_list[-1][1]] = 0

    for j in range(len(down_list) - 1):
        room_info[down_list[j][0]][down_list[j][1]] = room_info[down_list[j + 1][0]][down_list[j + 1][1]]
    room_info[down_list[-1][0]][down_list[-1][1]] = 0

def make_up_list():
    global up_list
    up_list = []
    for upy in range(up_wind-1, -1, -1):
        up_list.append((upy, 0))
    for upx in range(1, C):
        up_list.append((0, upx))
    for upy2 in range(1, up_wind + 1):
        up_list.append((upy2, C - 1))
    for upx2 in range(C - 2, 0, -1):
        up_list.append((up_wind, upx2))

def make_down_list():
    global down_list
    down_list = []
    for downy in range(down_wind + 1, R):
        down_list.append((downy, 0))
    for downx in range(1, C):
        down_list.append((R - 1, downx))
    for downy2 in range(R - 2, down_wind - 1, -1):
        down_list.append((downy2, C - 1))
    for downx2 in range(C - 2, 0, -1):
        down_list.append((down_wind, downx2))

# R : 행 개수, C : 열 개수, T : 시간 초
R, C, T = list(map(int, input().split()))
room_info = [list(map(int, input().split())) for _ in range(R)]

air_purifier = []

for y in range(R):
    for x in range(C):
        if room_info[y][x] == -1:
            air_purifier.append((y, x))

up_wind = air_purifier[0][0]
down_wind = air_purifier[1][0]

up_list = []
down_list = []

make_up_list()
make_down_list()

one_second(T)

result_value = 0
for y3 in range(R):
    for x3 in range(C):
        if room_info[y3][x3] >= 1:
            result_value += room_info[y3][x3]

print(result_value)
