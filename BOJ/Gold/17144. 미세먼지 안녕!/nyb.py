'''
https://www.acmicpc.net/problem/17144
'''


from collections import deque
# from pprint import pprint

BOARD_Y, BOARD_X, TIME = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(BOARD_Y)]


dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 공기청정기 위치 찾기
for i in range(BOARD_Y):
    if board[i][0] == -1:
        air_clean = [(i,0), (i+1,0)]
        break

# print(air_clean)

# 먼지확산
# 1. 먼지의 위치를 모두 큐에 넣기

deq = deque()

for i in range(BOARD_Y):
    for j in range(BOARD_X):
        if board[i][j] != 0:
            if board[i][j] == -1: continue
            deq.append((i,j))
# print(deq)

# pprint(board)

for _ in range(TIME):
    # 2. 상하좌우 동시 확산 -1인 경우 넘어감
    # 동시 처리를 위해 임시 보드 생성 후 값 저장
    temp_board = [[0] * BOARD_X for _ in range(BOARD_Y)]
    # pprint(temp_board)

    while deq:
        y, x = deq.popleft()
        temp_num = board[y][x]

        for dy, dx in dyx:
            ny, nx = y+dy, x+dx

            # 범위 체크
            if not (0 <= ny < BOARD_Y and 0 <= nx < BOARD_X): continue

            # 청정기 위치인 경우 확산 불가 스킵
            if board[ny][nx] == -1: continue

            # 숫자인 경우 확산
            temp_board[ny][nx] += temp_num // 5 # 임시 보드에 해당 칸에 쌓일 먼지 양 저장
            board[y][x] -= temp_num // 5    # 모체 먼지에서 확산된 양을 제거

    # 퍼진 값 기존 값에 더해주기
    for i in range(BOARD_Y):
        for j in range(BOARD_X):
            board[i][j] += temp_board[i][j]

    # pprint(temp_board)
    # pprint(board)

    # 청정기 바람으로 먼지 이동
    