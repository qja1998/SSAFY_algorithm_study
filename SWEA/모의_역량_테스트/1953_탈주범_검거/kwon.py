from collections import deque

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)
rev = (1, 0, 3, 2)

tunnel = [[],
          [1, 1, 1, 1],
          [1, 1, 0, 0],
          [0, 0, 1, 1],
          [1, 0, 0, 1],
          [0, 1, 0, 1],
          [0, 1, 1, 0],
          [1, 0, 1, 0]]

def fugitive_search(r, c):
    area_cnt = 1
    q = deque([(r, c)])
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1

    while q:
        y, x = q.popleft()

        for d in range(4):
            # 갈 수 있는 방향 확인
            if not tunnel[map_list[y][x]][d]:
                continue

            nx, ny = x + dx[d], y + dy[d]

            # 범위 나간 경우
            if not (0 <= nx < m and 0 <= ny < n):
                continue

            n_pos = map_list[ny][nx]
            # 벽 확인
            if not n_pos:
                continue
            # 방문한 경우
            if visited[ny][nx]:
                continue
            # 연결 안되는 경우
            if not tunnel[n_pos][rev[d]]:
                continue
            # 시간 초과
            if visited[y][x] + 1 > l:
                return area_cnt

            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))
            area_cnt += 1

    return area_cnt


test_case = int(input())

for t in range(test_case):
    # r, c: 맨홀
    n, m, r, c, l = map(int, input().split())

    map_list = [list(map(int, input().split())) for _ in range(n)]

    print(f"#{t + 1} {fugitive_search(r, c)}")