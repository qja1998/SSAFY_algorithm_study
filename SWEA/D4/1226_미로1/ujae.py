from collections import deque
 
def maze_bfs(maze, y, x):
    queue = deque([(y,x)])
    while queue:
        y, x = queue.popleft()
        for dy, dx in move:
            ny, nx = y+dy, x+dx
            if 0<= nx <16 and 0 <= ny <16 and (maze[ny][nx] == 0 or maze[ny][nx] == 3 or maze[ny][nx] == 2):
                queue.append((ny,nx))
                if maze[ny][nx] == 3:
                    return 1
                maze[ny][nx] = 1
    return 0
 
move = [[-1,0], [1,0], [0,-1], [0,1]]
 
for _ in range(10):
    T = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    for i in range(len(maze)):
        if 2 in maze[i]:
            start = [i, maze[i].index(2)]
            break
    y = start[0]
    x = start[1]
 
    print(f"#{T} {maze_bfs(maze, y, x)}")