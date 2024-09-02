from collections import deque

test_case =  int(input())

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

def dot2num(table, x, y):
    cnt = 0
    for i in range(8):
        tmp_x, tmp_y = x + dx[i], y + dy[i]
        if 0 <= tmp_x < n and 0 <= tmp_y < n and table[tmp_y][tmp_x] == '*':
            cnt += 1
    
    table[y][x] = cnt

def click(table, x, y):
    q = deque()
    q.append((x, y))
    table[y][x] = '*'

    while q:
        x, y = q.popleft()
        for i in range(8):
            tmp_x, tmp_y = x + dx[i], y + dy[i]
            if 0 <= tmp_x < n and 0 <= tmp_y < n:
                if table[tmp_y][tmp_x] == 0:
                    q.append((tmp_x, tmp_y))

                table[tmp_y][tmp_x] = '*'


for t in range(test_case):
    n = int(int(input()))

    table = []

    for i in range(n):
        table.append(list(input()))
    
    for y in range(n):
        for x in range(n):
            if table[y][x] == '.':
                dot2num(table, x, y)

    cnt = 0 
    for y in range(n):
        for x in range(n):
            if table[y][x] == 0:
                cnt += 1
                click(table, x, y)

    for y in range(n):
        for x in range(n):
            if table[y][x] != '*':
                cnt += 1
    print(f"#{t + 1} {cnt}")










from collections import deque


def bomb_mine(y, x, mine_map):
    queue = deque([(y, x)])
    while queue:
        y, x = queue.popleft()

        for dy, dx in move:
            ny = dy + y
            nx = dx + x
            if 0 <= ny < N and 0 <= nx < N:
                if mine_map[ny][nx] == '.':
                    queue.append((ny, nx))
                elif mine_map[ny][nx] == 1:
                    mine_map[ny][nx] = 2
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