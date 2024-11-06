from collections import deque


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우


def log(arr):
    for lst in arr:
        for elem in lst:
            print(elem, end=" ")
        print()
    print()


def bfs(grid, grid_size, sx, sy):
    # log(grid)
    queue = deque([(sx, sy)])  # 시작지점 x, 시작지점 y
    grid[sx][sy] = 1  # 방문 표시
    conn_len = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= grid_size or ny < 0 or ny >= grid_size:
                continue
            if grid[nx][ny]:
                continue

            grid[nx][ny] = 1
            queue.append((nx, ny))
            conn_len += 1

    return conn_len


def main():
    N, M, K = map(int, input().split())  # N: 칸 수, M: 포자 수, K: 최대 연결 수
    farm = [list(map(int, input().split())) for _ in range(N)]

    used_poza = 0
    for i in range(N):
        for j in range(N):
            if farm[i][j] == 0:  # 버섯이 자랄 수 있는 영역
                # log(farm)
                # 하나의 연결된 영역에 버섯이 몇 개 필요한지 세기
                connected_len = bfs(farm, N, i, j)  # 연결된 영역의 길이
                used_poza += (connected_len // K)  # conn_len은 x*K 만큼 커버가능 => K개로 나눈 몫이 x가 됨
                used_poza += 1 if (connected_len % K) else 0  # 나머지 존재하면 하나 더

    if used_poza and M-used_poza > 0:
        print(f"POSSIBLE\n{M-used_poza}")
    else:
        print("IMPOSSIBLE")


if __name__ == "__main__":
    main()