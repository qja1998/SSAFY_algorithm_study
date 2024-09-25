from collections import deque
 
 
def bomb_mine(y, x, mine_map):
    global visited
    queue = deque([(y, x)])
    visited.add((y,x))
    while queue:
        y, x = queue.popleft()
 
        for dy, dx in move:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited:
                if mine_map[ny][nx] == '.':
                    queue.append((ny, nx))
                    visited.add((ny, nx))
                elif mine_map[ny][nx] == 1:
                    mine_map[ny][nx] = 2
                    visited.add((ny, nx))
                else:
                    continue
 
        mine_map[y][x] = 2
 
 
T = int(input())
 
move = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
 
for test_case in range(1, T+1):
    N = int(input())
 
    mine_map = [list(map(str, input().rstrip())) for _ in range(N)]
 
    count = 0
 
    one_num = set()
    visited = set()
    for y in range(N):
        for x in range(N):
            if mine_map[y][x] == '*':
                for dy, dx in move:
                    ny = dy + y
                    nx = dx + x
                    if 0 <= ny <= N-1 and 0 <= nx <= N-1:
                        if mine_map[ny][nx] != '*':
                            mine_map[ny][nx] = 1
                            one_num.add((ny, nx))
 
    for y in range(N):
        for x in range(N):
            if mine_map[y][x] == '.':
                bomb_mine(y, x, mine_map)
                count += 1
 
    for y, x in one_num:
        if mine_map[y][x] == 1:
            count += 1
 
    print(f'#{test_case} {count}')