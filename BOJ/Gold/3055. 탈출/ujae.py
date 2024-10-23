# 1. 사악한 암흑의 군주 이민혁 드디어 마법의 구슬 손에 넣다
# 2. 티떱숲에 홍수 일으키고 싶다.
# 3. 숲에 고슴도치 사는중
# 4. 고슴도치 짱친 비버굴로 도망치고 싶음
# ----------------------------------------------------------------------------------
# 1. 티떱숲 R행 C열
# 2. 비어있는 곳 = .
# 3. 물이 차있는 지역 = *
# 4. 돌 = X
# 5. 비버의 굴 = D
# 6. 고슴도치의 위치 = S
# 7. 매 분마다 고슴도치는 현재 있는 칸과 인접한 네 칸 중 하나로 이동가능
# 8. 매 분마다 물도 비어있는 칸으로 확장 = 물은 bfs인듯
# 9. 고슴도치는 물 있는 구역으로 이동 불가능
# 10. 물은 비버  소굴로 이동 불가능
# 11. 고슴도치는 물이 찰 예정인 구역도 이동 불가능
# -----------------------------------------------------------------------------------
# 1. 출력 : 고슴도치가 비버의 굴로 이동할 수 있는 가장 빠른 시간. 이동x = KAKTUS
# 2. 입력
# 	2.1) R C
# 	2.2) R개 줄에 티떱숲의 지도

from collections import deque

move = ((-1, 0), (1, 0), (0, 1), (0, -1))

R, C = list(map(int, input().split()))
forest_info = [list(map(str, input().rstrip())) for _ in range(R)]
water_info = [[R*C] * C for _ in range(R)]

water_start = deque([])
rock_info = []

for y in range(R):
    for x in range(C):
        if forest_info[y][x] == 'D':
            biber_house = (y, x)
        elif forest_info[y][x] == 'X':
            rock_info.append((y, x))
        elif forest_info[y][x] == '*':
            water_start.append((y, x))
            water_info[y][x] = 0
        elif forest_info[y][x] == 'S':
            hedgehog_info = (y, x)
            forest_info[y][x] = 0


def water_move(queue):
    while queue:
        now = queue.popleft()
        for dy, dx in move:
            ny = dy + now[0]
            nx = dx + now[1]
            if 0 <= ny < R and 0 <= nx < C:
                if water_info[ny][nx] == R*C and forest_info[ny][nx] != 'X' and forest_info[ny][nx] != 'D':
                    water_info[ny][nx] = water_info[now[0]][now[1]] + 1
                    queue.append((ny, nx))


def hedgehog_move(y_, x_):
    hedge_queue = deque([(y_, x_)])

    while hedge_queue:
        now = hedge_queue.popleft()
        for dy, dx in move:
            ny = dy + now[0]
            nx = dx + now[1]
            if 0 <= ny < R and 0 <= nx < C:
                if forest_info[ny][nx] == '.' and (forest_info[now[0]][now[1]] + 1) < water_info[ny][nx]:
                    forest_info[ny][nx] = forest_info[now[0]][now[1]] + 1
                    hedge_queue.append((ny, nx))
                elif forest_info[ny][nx] == 'D':
                    forest_info[ny][nx] = forest_info[now[0]][now[1]] + 1
                    return


water_move(water_start)
hedgehog_move(hedgehog_info[0], hedgehog_info[1])

if forest_info[biber_house[0]][biber_house[1]] == 'D':
    print("KAKTUS")
else:
    print(forest_info[biber_house[0]][biber_house[1]])



# def water_move(queue):
#     while queue:
#         now = queue.popleft()
#         for dy, dx in move:
#             ny = dy + now[0]
#             nx = dx + now[1]
#             if 0 <= ny < R and 0 <= nx < C:
#                 if water_info[ny][nx] == -1 and forest_info[ny][nx] != 'X':
#                     water_info[ny][nx] = water_info[now[0]][now[1]] + 1
#                     queue.append((ny, nx))
#
#
# def hedgehog_move(y_, x_):
#     queue = deque([(y_, x_)])
#
#     while queue:
#         now = queue.popleft()
#         for dy, dx in move:
#             ny = dy + now[0]
#             nx = dx + now[1]
#             if 0 <= ny < R and 0 <= nx < C:
#                 if forest_info[ny][nx] == '.' and ((forest_info[now[0]][now[1]] + 1) < water_info[ny][nx]):
#                     forest_info[ny][nx] = forest_info[now[0]][now[1]] + 1
#                     queue.append((ny, nx))
#                 elif forest_info[ny][nx] == 'D':
#                     forest_info[ny][nx] = forest_info[now[0]][now[1]] + 1
#                     return
#
#
# R, C = list(map(int, input().split()))
# forest_info = [list(map(str, input().rstrip())) for _ in range(R)]
# water_info = [[-1] * C for _ in range(R)]
# water_start = deque([])
# for y in range(R):
#     for x in range(C):
#         if forest_info[y][x] == '*':
#             water_start.append((y, x))
#             water_info[y][x] = 0
#
# pan2 = 0
# for y2 in range(R):
#     for x2 in range(C):
#         if forest_info[y2][x2] == 'D':
#             biber_house = (y2, x2)
#             pan2 = 1
#             break
#     if pan2 == 1:
#         break
#
# # --------물 이동 끝----------
# pan1 = 0
# for y1 in range(R):
#     for x1 in range(C):
#         if forest_info[y1][x1] == 'S':
#             hedgehog_start = (y1, x1)
#             pan1 = 1
#             break
#     if pan1 == 1:
#         break
# # ---------고슴도치 이동 끝----------------------
#
#
# water_move(water_start)
# forest_info[hedgehog_start[0]][hedgehog_start[1]] = 0
# hedgehog_move(hedgehog_start[0], hedgehog_start[1])
#
# if forest_info[biber_house[0]][biber_house[1]] == 'D':
#     print("KAKTUS")
# else:
#     print(forest_info[biber_house[0]][biber_house[1]])
