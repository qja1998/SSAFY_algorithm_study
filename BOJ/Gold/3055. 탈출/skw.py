from collections import deque

direction = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs():
    while w_queue or s_queue:
        for _ in range(len(w_queue)):
            crt_x, crt_y = w_queue.popleft()
            for dx, dy in direction:
                nx, ny = crt_x + dx, crt_y + dy
                if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    w_queue.append((nx, ny))

        for _ in range(len(s_queue)):
            crt_x, crt_y = s_queue.popleft()
            for dx, dy in direction:
                nx, ny = crt_x + dx, crt_y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    if graph[nx][ny] == 'D':
                        return visited[crt_x][crt_y]
                    if graph[nx][ny] == '.':
                        graph[nx][ny] = 'S'
                        visited[nx][ny] = visited[crt_x][crt_y] + 1
                        s_queue.append((nx, ny))
    return 'KAKTUS'

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
w_queue = deque()
s_queue = deque()
visited = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S':
            s_queue.append((i, j))
            visited[i][j] = 1
        elif graph[i][j] == '*':
            w_queue.append((i, j))

result = bfs()
print(result)