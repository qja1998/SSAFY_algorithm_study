from collections import deque

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(dir):
    cnt = 1

    while queue:
        x, y = queue.popleft()
        flag = 0

        for _ in range(4):
            dir = (dir + 3) % 4
            nx, ny = x + direction[dir][0], y + direction[dir][1]
            if 0 <= nx < n and 0 <= ny < m and not graph[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
                    flag = 1
                    break
        if not flag:
            if graph[x - direction[dir][0]][y - direction[dir][1]] != 1:
                queue.append((x - direction[dir][0], y - direction[dir][1]))
            else:
                return cnt
    return


n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

queue = deque([(r, c)])
visited[r][c] = 1

result = bfs(d)
print(result)