N = 16
START = 2
END = 3
WALL = 0

test_case = 10

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def chk_pos(x, y):
    return 0 <= x < N and 0 <= y < N and (maze[y][x] == 0 or maze[y][x] == 3)

def dfs(x, y):
    if maze[y][x] == 3:
        global chk_find
        chk_find = 1
        return
    
    if chk_find == 1:
        return
    
    maze[y][x] = -1
    for i in range(4):
        x_next, y_next = x + dx[i], y + dy[i]
        if chk_pos(x_next, y_next):
            dfs(x_next, y_next)
        

for _ in range(test_case):
    maze = []
    t = int(input())
    for _ in range(N):
        maze.append([int(s) for s in input()])

    chk_find = 0

    for y, row in enumerate(maze):
        if 2 in row:
            start_x = row.index(2)
            start_y = y
            break

    dfs(start_x, start_y)

    print(f"#{t} {chk_find}")