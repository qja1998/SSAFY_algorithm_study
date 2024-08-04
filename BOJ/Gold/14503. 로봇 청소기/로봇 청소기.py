n, m = map(int, input().split()) # 세로, 가로

y, x, d = map(int, input().split()) # y, x, d

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

# i 감소하면 반시계 회전
# N, E, S, W
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

room[y][x] = -1
clean_num = 1

while True:
    clean_chk = False
    for i in range(4):
        d = (d + 3) % 4
        front_x = x + dx[d]
        front_y = y + dy[d]

        if (0 <= front_x < m) and (0 <= front_y < n):
            if room[front_y][front_x] == 0:
                x, y = front_x, front_y
                room[y][x] = -1
                clean_num += 1
                clean_chk =True
                break
    
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if not clean_chk:
        back_d = (d + 2) % 4
        back_x = x + dx[back_d]
        back_y = y + dy[back_d]

        if (0 <= back_x < m) and (0 <= back_y < n):
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
            if room[back_y][back_x] != 1:
                x, y = back_x, back_y
            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
            else:
                break
        else:
            break

print(clean_num)