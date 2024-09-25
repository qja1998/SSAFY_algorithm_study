import sys
sys.stdin = open('3_input.txt', 'r')

from collections import deque

# 메인 함수
def tomato(toma, st_toma):
    # 사방탐색
    dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # 큐가 빌 때까지
    while st_toma:
        # 첫번째 요소꺼내서 x,y에 담기
        x, y = st_toma.popleft()
        # 사방탐색 시작
        for dir in dxy:
            nx = x + dir[0]
            ny = y + dir[1]
            # 배열 범위를 벗어난다면 지나가기
            if 0 > nx or nx >= N or 0 > ny or ny >= M:
                continue
            # 아직 안익은 토마토라면
            if toma[nx][ny] == 0:
                # 영향받을 토마토에 영향받은 토마토 익은시간 +1
                toma[nx][ny] = toma[x][y]+1
                # 큐에 추가
                st_toma.append([nx, ny])

    # 전체를 돌면서 안익은 토마토 찾기
    for i in range(N):
        for j in range(M):
            if toma[i][j] == 0:
                res = -1
                return res

    # 다 익었으면 얼마나 걸렸는지 계산
    res = max(map(max, toma)) - 1
    return res

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    M, N = map(int, input().split())
    toma = list(list(map(int, input().split())) for _ in range(N))

    # 익은 토마토 담을 리스트 만들기
    # 출발지가 들어있는 큐 만들기
    st_toma = deque([])
    # 전체를 돌면서 익은 토마토 찾기
    for i in range(N):
        for j in range(M):
            # 익은 토마토 표시라면
            if toma[i][j] == 1:
                # 익은 토마토 위치 저장
                st_toma.append([i, j])

    # 메인 함수 시작
    ans = tomato(toma, st_toma)

    print(ans)