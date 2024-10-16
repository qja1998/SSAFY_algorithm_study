from collections import defaultdict
N, M = map(int, input().split())

game_map = [input() for _ in range(N)]

dyx = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def show(y, x):
    show_mat = [[0]*M for _ in range(N)]

    show_mat[y][x] = 1
    return show_mat

visited = defaultdict(bool)
def dfs(dot, x, y, pre, cnt=1):
    
    for dy, dx in dyx:
        ny, nx = y + dy, x + dx
        if not(0 <= ny < N and 0 <= nx < M):
            continue
        if visited[(ny, nx)]:
            if game_map[ny][nx] == dot and pre != (nx, ny) and cnt >= 4:
                return True
            continue
        # 같은 값의 점이 아님
        if game_map[ny][nx] != dot:
            continue
        visited[(ny, nx)] = True
        if dfs(dot, nx, ny, (x, y), cnt+1):
            return True
        
available = False
for y in range(N):
    for x in range(M):
        if visited[(y, x)]:
            continue
        if dfs(game_map[y][x], x, y, (-1, -1)):
            available = True
            break
    if available:
        break

print('Yes' if available else 'No')