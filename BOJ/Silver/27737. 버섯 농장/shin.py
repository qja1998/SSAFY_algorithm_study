import math as m
from collections import deque

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(cnt_x, cnt_y):
    global M

    queue = deque([(cnt_x, cnt_y)])
    m_area = 1
    graph[cnt_x][cnt_y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + direction[i][0]
            ny = y + direction[i][1]

            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                m_area += 1
                queue.append((nx, ny))

    M -= m.ceil(m_area/K)


N, M, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
check = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 0:
            check += 1
            bfs(i, j)

print(f'POSSIBLE\n{M}' if M >= 0 and check > 0 else 'IMPOSSIBLE')