directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]


def dfs(x, y, dir_index, cnt):
    global max_desserts
    if not (0 <= x < N and 0 <= y < N) or dir_index > 3:
        return
    if dir_index == 3 and (x, y) == (start_x, start_y):
        max_desserts = max(cnt, max_desserts)
        return
    if visited[dessert_map[x][y]]:
        return
    visited[dessert_map[x][y]] = True
    nx, ny = x + directions[dir_index][0], y + directions[dir_index][1]
    dfs(nx, ny, dir_index, cnt + 1)
    dfs(nx, ny, dir_index + 1, cnt + 1)
    visited[dessert_map[x][y]] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    dessert_map = [list(map(int, input().split())) for _ in range(N)]
    max_desserts = -1
    visited = [False] * 101

    for start_x in range(N):
        for start_y in range(N):
            dfs(start_x, start_y, 0, 0)

    print(f"#{tc} {max_desserts}")
