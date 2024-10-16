from collections import deque

move = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(start_y, start_x):
    queue = deque([(start_y, start_x, -1, -1)])
    visited[start_y][start_x] = True

    while queue:
        y, x, from_y, from_x = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if (ny, nx) == (from_y, from_x):
                    continue
                if alphabet_list[ny][nx] == alphabet_list[y][x]:
                    if visited[ny][nx]:
                        return True
                    visited[ny][nx] = True
                    queue.append((ny, nx, y, x))
    return False


N, M = map(int, input().split())
alphabet_list = [input().strip() for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            if bfs(y, x):
                print("Yes")
                exit()

print("No")