# 입력 받기
N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

# 청소를 기록할 visited 배열 생성
visited = [[0] * M for _ in range(N)]

# 현재 위치 청소
visited[r][c] = 1
clean_count = 1

while True: 
    found = False

    # 4방향 모두 확인
    for _ in range(4):
        d = (d - 1) % 4  # 반시계 방향으로 회전
        nx = r + dx[d]
        ny = c + dy[d]

        # 회전한 방향에 청소할 공간이 있다면 이동
        if room[nx][ny] == 0 and visited[nx][ny] == 0:
            r, c = nx, ny
            visited[r][c] = 1
            clean_count += 1
            found = True
            break

    # 4방향 모두 청소가 되어 있거나 벽일 때
    if not found:
        # 후진할 방향 계산
        back_x = r - dx[d]
        back_y = c - dy[d]

        # 후진 가능하면 후진
        if room[back_x][back_y] == 0:
            r, c = back_x, back_y
        else:
            # 후진 불가, 종료
            break

# 청소한 칸의 개수 출력
print(clean_count)
