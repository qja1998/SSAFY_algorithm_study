from copy import deepcopy
from collections import deque, defaultdict

def _debug_matrix(matrix):
    return list(zip(*matrix[::-1]))

def remove_block(matrix, x, y):
    block_num = matrix[x][y]
    if matrix[x][y] == 0:
        return None, None
    
    q = deque([(x, y, matrix[x][y])])
    visited = defaultdict(bool)
    visited[(x, y)] = True
    
    cnt = 0
    while q:
        x, y, block_num = q.popleft()
        cnt += 1

        matrix[x][y] = 0
        
        for i in range(1, block_num):

            # 오른쪽
            if x+i < w and matrix[x+i][y] != 0 and not visited[(x+i, y)]:
                q.append((x+i, y, matrix[x+i][y]))
                matrix[x+i][y] = 0
                visited[(x+i, y)] = True

            # 왼쪽
            if x-i >= 0 and matrix[x-i][y] != 0 and not visited[(x-i, y)]:
                q.append((x-i, y, matrix[x-i][y]))
                matrix[x-i][y] = 0
                visited[(x-i, y)] = True

            # 위
            if y+i < h and matrix[x][y+i] != 0 and not visited[(x, y+i)]:
                q.append((x, y+i, matrix[x][y+i]))
                matrix[x][y+i] = 0
                visited[(x, y+i)] = True

            # 아래
            if  y-i >= 0 and matrix[x][y-i] != 0 and not visited[(x, y-i)]:
                q.append((x, y-i, matrix[x][y-i]))
                matrix[x][y-i] = 0
                visited[(x, y-i)] = True
    
    # 터진 곳 처리
    for x in range(w):
        y = 0
        while matrix[x][y:] != [0] * len(matrix[x][y:]):
            if matrix[x][y] != 0:
                y += 1
                continue
            matrix[x].pop(y)
            matrix[x].append(0)
    
    return matrix, cnt

def find_num(arr):
    for i in range(h-1, -1, -1):
        if arr[i] > 0:
            return i
    return -1

def drop_ball(matrix, n, x, y, cnt = 0):
    global max_block
    if n == 0 or matrix == all_zero:
        max_block = max(max_block, cnt)
        return
    
    n_matrix, cnt_block = remove_block(deepcopy(matrix), x, y)
    if not n_matrix and not cnt_block:
        return
    cnt += cnt_block

    if n_matrix == all_zero:
        max_block = max(max_block, cnt)
        return

    for nx in range(w):
        ny = find_num(n_matrix[nx])
        if ny == -1:
            continue
        drop_ball(n_matrix, n-1, nx, ny, cnt)

test_case = int(input())

for t in range(test_case):
    n, w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]
    
    # 시계방향 90도 회전
    matrix = list(zip(*matrix[::-1]))
    matrix = [list(row) for row in matrix]
    all_zero = [[0]*h for _ in range(w)]

    total_cnt = 0
    for row in matrix:
        for num in row:
            if num != 0:
                total_cnt += 1

    max_block = 0

    for x in range(w):
        y = find_num(matrix[x])
        if y == -1:
            continue
        drop_ball(matrix, n, x, y)

    print(f"#{t+1} {total_cnt - max_block}")
