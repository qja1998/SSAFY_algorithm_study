from collections import deque

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for _ in range(10):
    MAZE_SIZE = 16
    START_POS = (1, 1)
    END_POS = (13, 13)
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(MAZE_SIZE)]
    result = 0
    visited = [[False] * MAZE_SIZE for _ in range(MAZE_SIZE)]

    queue = deque([START_POS])
    while queue:
        ci, cj = queue.popleft()

        FLAG = False
        for dx, dy in dxy:
            ni, nj = ci + dx, cj + dy

            if ni < 0 or ni >= MAZE_SIZE or nj < 0 or nj >= MAZE_SIZE: continue

            if visited[ni][nj]: continue

            if maze[ni][nj] == 1: continue

            queue.append((ni, nj))
            visited[ni][nj] = True

            if (ni, nj) == END_POS:
                result = 1
                FLAG = True
                break
        if FLAG:
            break

    print(f"#{tc} {result}")
