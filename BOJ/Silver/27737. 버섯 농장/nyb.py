from collections import deque

BOARD_SIZE, m_cnt, K = map(int, input().split())
wolrae_m_cnt = m_cnt
board = [list(map(int, input().split())) for _ in range(BOARD_SIZE)]
# print(board)

dyx = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# board에서 버섯이 자랄 수 있는 공간의 크기를 찾는 함수
def search(point):
    global board
    global m_cnt
    cnt = 0 # 버섯 재배 공간 크기

    deq = deque([point])
    board[point[0]][point[1]] = 1

    while deq:
        cy, cx = deq.popleft()
        cnt += 1    # 버섯 재배 공간 카운트

        for dy, dx in dyx:
            ny, nx = cy + dy, cx + dx

            if not (0 <= ny < BOARD_SIZE and 0 <= nx < BOARD_SIZE): continue

            if board[ny][nx] == 1: continue

            # 새 지점이 0이면
            if board[ny][nx] == 0:
                deq.append((ny, nx))
                board[ny][nx] = 1  # 방문 체크

    # 버섯 재배 공간 크기를 구했다!
    # print(cnt)
    if cnt <= K:
        m_cnt -= 1
    else:
        # 배수 관계라면
        if cnt % K == 0:
            m_cnt -= cnt // K
        else:
            m_cnt -= cnt // K +1


for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        if board[i][j] == 0:
            search((i, j))

if m_cnt == wolrae_m_cnt:
    print('IMPOSSIBLE')
elif m_cnt >= 0 :
    print('POSSIBLE')
    print(m_cnt)
else:
    print('IMPOSSIBLE')