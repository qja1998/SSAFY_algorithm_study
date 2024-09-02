TC = int(input())

from collections import defaultdict, deque

dyx = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def inf():
    return float('inf')

for t in range(1, TC+1):
    N, M = map(int, input().split())

    matrix = [list(input()) for _ in range(N)]

    distances = [[float('inf')]*M for _ in range(N)]
    water_list = []

    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 'W':
                water_list.append((y, x))
                distances[y][x] = 0

    # 모두 물이거나 땅
    if len(water_list) == 0 or len(water_list) == N*M:
        print(f"#{t} 0")
        continue

    # distances = defaultdict(inf)
    
    for water in water_list:
        q = deque([water])
        # print(q)
        while q:
            y, x = q.popleft()

            for dy, dx in dyx:
                ny, nx = y + dy, x + dx
                # 범위 벗어날 때
                if nx < 0 or nx >= M or ny < 0 or ny >= N:
                    continue
                
                if distances[y][x] != float('inf') or distances[y][x] != 0:
                    continue

                # 거리 갱신
                distances[ny][nx] = distances[y][x] + 1
                q.append((ny, nx))

    for row in distances:
        print(row)

    # print(f"#{t} {sum(distances.values())}")
    print(f"#{t} {sum(map(sum, distances))}")



# from collections import deque

# for tc in range(1, int(input()) + 1):
#     n, m = map(int, input().split())
#     visited = [[-1] * m for _ in range(n)]
#     _map = []
#     q = deque()
#     for i in range(n):
#         tmp = input()
#         for j in range(m):
#             if tmp[j]=='W':
#                 q.append((i, j))
#                 visited[i][j] = 0

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     def bfs():
#         while q:
#             x, y = q.popleft()
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
#                 if visited[nx][ny] != -1: continue
#                 q.append((nx, ny))
#                 visited[nx][ny] = visited[x][y] + 1

#     bfs()
#     for row in visited:
#         print(row)
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             result += visited[i][j]
#     print("#{} {}".format(tc, result))