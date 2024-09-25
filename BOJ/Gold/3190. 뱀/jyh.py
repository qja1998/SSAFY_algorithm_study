import sys
sys.stdin = open('4_input.txt', 'r')

from collections import deque

# 메인 함수
def game(borad):
    global time, ndxy
    # 뱀만들기
    sn_len = 1
    snake = deque([(0, 0)])
    # 뱀 시작 체크
    x, y = 0, 0  # deque([0, 0])
    borad[x][y] = 9
    # 뱀이 있는 동안 계속 실행
    while snake:
        # 방향을 바꿀 차례라면 방향 정보 뽑아오기
        if time == int(way[0][0]):
            a, b = way.pop(0)
            if b == 'L':
                ndxy += 1
                ndxy %= 4
            # 아니라면 dxy인덱스 정보 우하좌상
            else:
                ndxy -= 1
                ndxy %= 4

        # 방향 찾기
        cx, cy = dxy[ndxy]
        # 다음 위치 찾기
        nx, ny = x + cx, y + cy
        # 다음 위치가 범위를 벗어난다면 게임종료
        if 0 > nx or nx >= N or 0 > ny or ny >= N:
            return time + 1

        # 사과 못먹으면 꼬리 당기고 몸길이 늘리기
        if borad[nx][ny] != 1:
            # 진행할 다음 위치에 뱀이 있다면 게임종료
            if borad[nx][ny] == 9:
                return time + 1
            borad[nx][ny] = 9
            # 진행 가능하다면 꼬리 당겨오기
            lx, ly = snake.popleft()
            borad[lx][ly] = 0
            snake.append([nx, ny])
        else:
            # 진행할 다음 위치에 뱀이 있다면 게임종료
            if borad[nx][ny] == 9:
                return time + 1
            borad[nx][ny] = 9
            # 사과 먹으면 꼬리 안당기기. 몸길이 늘려
            sn_len += 1
            snake.append([nx,ny])

        # 뱀 머리 다시 확인해주기위치 뽑기
        x, y = snake[sn_len-1]

        time += 1

# 주어진 입력받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    K = int(input())
    apple = [list(map(int, input().split())) for _ in range(K)]
    L = int(input())
    way = [list(input().split()) for _ in range(L)]
    way.append([0, 0])

    # 보드 만들기
    borad = [[0] * N for _ in range(N)]
    # 사과 위치 표시
    for x, y in apple:
        borad[x-1][y-1] = 1

    # 시간 늘려줄 변수
    time = 0

    # 우상좌하
    dxy = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    # 어느 방향인지
    ndxy = 0

    # 메인 함수 시작
    ans = game(borad)

    print(ans)