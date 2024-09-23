from collections import deque

# N (뱀 게임할 보드의 크기 입력 받기)
N = int(input())
# K (보드 위에 존재할 사과의 갯수 입력 받기)
K = int(input())
# 사과의 위치 값 K 개 만큼 입력 받기
apple_location = [list(map(int, input().split())) for _ in range(K)]
# L (뱀의 방향 이동 횟수 입력 받기)
L = int(input())
# 방향 이동 횟수 만큼 이동 방향과, 몇 초 후에 이동할 것인지 입력 받기, 이때 형식 (방향 이동 예정 시간, 이동 방향)
change_info = [list(map(str, input().split())) for _ in range(L)]

# 디버깅을 위한 함수 from 스터디장님.
# pycharm 에서 디버그 누르면 아래에 Debugger 과 Console 창이 뜸
# 이때 Debugger를 누르면 아래쪽에 Frames 와 Variables가 뜸
# Variables에서 + 버튼을 누르고 show_map을 입력 하면 해당 값을 볼 수 있음
# 현재 show_map은 N*N의 보드 맵을 표현하고 있으며 뱀의 위치를 1, 그 외 뱀이 위치하지 않은곳을 0으로 표현
# matrix는 N*N의 보드, y랑 x의 위치에 따라 1로 표현 매 순간마다 return matrix를 통해 맵 표현
def show_map(snake):
    matrix = [[0] * N for _ in range(N)]
    for y, x in snake:
        matrix[y][x] = 1
    return matrix

# move의 형식 : 첫 이동 방향은 무조건 오른쪽 이니까 (0, 1)
# 오른쪽으로 회전할 시 (1, 0)/아래 방향, 그 다음에 또 오른쪽으면 (0, -1)/왼쪽 이렇게 index 값을 1개씩 만 오른쪽으로 옮기면 오른쪽으로 도는 방향임
# 만약 왼쪽으로 방향 전환 시 index값을 -1 하면 왼쪽 방향이 됨
# 즉 해당 이동 방향에 맞게 move 를 설정
move = ((0, 1), (1, 0), (0, -1), (-1, 0))

# snake를 deque로 생성 : 뱀의 이동을 queue에 머리를 나타내는 좌표를 append 하고
# 꼬리를 나타내는 좌표를 popleft 해서 나타낼 것이기 때문
snake = deque([(0, 0)])
# count : 게임이 진행된 시간
count = 0
# way : 방향을 나타냄 / 즉, move의 index를 나타낼 값 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
way = 0
# pan = 0 / 안쓰는 값음
# 방향을 이동 하는건 (시작 후 몇 초 뒤, 이동 방향) 여기서 "시작 후 몇 초 뒤" 이기 때문에 이전에 방향을 바꾸고 해당 시간 후에
# 다시 방향을 전환하는 것은 아님, 그렇기에 현재까지 얼마만큼의 시간이 경과 했는지 판단하려고 했음
# 물론 count로 계산 할 수도 있겠지만 직관적으로, count는 결과 값, time_cum은 계산하기 위한 변수로 보기 위해 다음과 같이 했음
time_cum = 0
# change_info 즉, L만큼 반복
for time, path in change_info:
    # 이동을 위해 y와 x에 더해줄 값
    dy = move[way][0]
    dx = move[way][1]
    # 할당 된 시간만큼 반복, 이때 int(time)-time_cum에서 int(time)은 현재 방향 전환이 시작 후 몇초후에 실행되는가
    # time_cum은 이전에 방향을 바꿨던 시간을 나타냄, 즉 이번이 시작 후 13초 후, 이전이 시작 후 10초 후면 13-10해서 3초 동안만 반복함
    for _ in range(int(time) - time_cum):
        # ny와 nx는 이동할 위치, snake[-1]에 대해 접근하는 이유는 머리 좌표를 보기 위함
        # snake[0]이 가리키는 것은 꼬리 좌표, snake[-1]이 가리키는 것은 머리 좌표
        # 즉, 머리가 이동하기 때문에 머리에서 접근함
        ny, nx = dy + snake[-1][0], dx + snake[-1][1]
        # 만약 보드판 범위 밖이라면
        if not (0 <= ny < N) or not (0 <= nx < N):
            # 머리가 이동해서 벽에 부딪혀야 끝나기 때문에 count += 1 해주고 끝냄
            count += 1
            print(count)
            exit()
        # 만약 보드판 범위 안이라면
        else:
            # 현재 문제에서 사과 좌표는 파이썬의 배열에서 인덱스 접근처럼 0부터 하는 것이 아닌 좌표 1부터 접근함
            # 그렇기에 올바른 사과 좌표값을 가리키기 위해 y와 x에 1씩 더해서 접근함
            # 만약 해당 좌표에 사과가 있다면
            if [ny + 1, nx + 1] in apple_location:
                # 해당 사과 좌표를 사과 좌표값을 저장한 리스트에서 지우고
                apple_location.remove([ny + 1, nx + 1])
                # 뱀의 머리 위치를 옮기고, 꼬리 좌표는 popleft 해주지 않음, 사과를 먹어서 뱀의 길이가 증가했기때문
                snake.append((ny, nx))
                # 게임 경과 시간 +1 해주기
                count += 1
            # 만약 해당 좌표에 사과가 없다면
            else:
                # 게임 경과 시간 +1 해주기
                count += 1
                # 근데 머리가 이동했을때 그 좌표가 뱀의 몸통일 경우 게임 종료
                if (ny, nx) in snake:
                    print(count)
                    exit()
                # 머리가 이동했을때 그 좌표가 뱀의 몸통이 아닐 경우 (ny, nx)/머리가 이동할 좌표 를 뱀queue에 append 
                snake.append((ny, nx))
                # 사과를 먹지 못해 뱀의 길이가 늘어나지 않았으므로 꼬리 pop해주기
                snake.popleft()
                # 게임을 전반적으로 봤을때 머리를 먼저 이동해주고 꼬리를 이동해줘야하기 때문에
                # 머리 이동 후, 종료 조건 판별, 그리고 꼬리 좌표 pop해주기

    # 이동 방향에 L이면 왼쪽 방향으로 돌아야함
    # 방향을 나타내는 값인 way에 대해 -1 해주고 %4를 해주면 이동 방향에 대한 index가 나옴
    if path == 'L':
        # python 은 음수%정수 했을때 양수가 나옴. 음수를 나눌 수 있을 정도의 크기로 올려준다음 나누기하면 몫은 음수
        # 그리고 올려준만큼 나머지가 됨
        # 여기서 음수를 나눌 수 있을 정도의 크기로 올려준다는 것은 -5를 4로 나누려 했을때 -5는 4로 나누어 떨어지지 않음
        # 그렇기에 -5를 -8로 바꾸고 4로 나누어 준다는 것
        # 이때 몫은 -2 이고 나머지는 3임, 쉽게 이해하자면 -5 => -8 -3만큼 더해줌, 이때 나머지는 더해준 만큼 다시 빼주면 됨
        # 즉, 나머지는 3이 됨
        way = (way - 1) % 4
    # 이동 방향이 L이 아니면 오른쪽으로 회전해야 함, index+1 해주면 오른쪽 회전을 나타냄
    else:
        way = (way + 1) % 4
    # 이전 경우의 시간 값을 저장
    time_cum = int(time)

# 현재 위의 반복문 에서는 주어진 방향 전환 조건에 대해서만 처리함
# 만약 위의 조건 후에도 게임이 끝나지 않는다면 벽이나 몸통에 박아서 끝나야 함
# 단, 이때 이동은 방향 전환 없이 마지막 이동 방향에 대해 계속 이동하면 되기 때문에 while True로 접근
dy = move[way][0]
dx = move[way][1]
while True:
    # 이동 방향에 대해 계속 더해줌
    ny, nx = dy + snake[-1][0], dx + snake[-1][1]
    # 범위 끝을 만나면 게임 종료
    if not (0 <= ny < N) or not (0 <= nx < N):
        count += 1
        print(count)
        exit()
    # 아닐 시 종료 조건을 만족할 때까지 반복
    else:
        if [ny + 1, nx + 1] in apple_location:
            apple_location.remove([ny + 1, nx + 1])
            snake.append((ny, nx))
            count += 1
        else:
            count += 1
            if (ny, nx) in snake:
                print(count)
                exit()
            snake.append((ny, nx))
            snake.popleft()