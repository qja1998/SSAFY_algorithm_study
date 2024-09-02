dx = [-1, 0, 0]
dy = [0, -1, 1]

def search_leader(x, y):
    while x != 0:
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 100 and 0 <= ny < 100 and ladder_arr[nx][ny]:
                ladder_arr[x][y] = 0  # 현재 위치를 방문한 것으로 표시
                x, y = nx, ny
    return y

for _ in range(1, 11):
    tc = int(input())
    result = 0
    ladder_arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if ladder_arr[99][i] == 2:
            result = search_leader(99, i)
            break

    print(f"#{tc} {result}")