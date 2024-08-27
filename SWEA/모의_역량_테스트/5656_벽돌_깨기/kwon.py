from copy import deepcopy
from collections import deque, defaultdict

def _debug_matrix(matrix):
    return list(zip(*matrix[::-1]))

def remove_block(matrix, x, y):
    block_num = matrix[x][y]
    if matrix[x][y] == 0:
        return None, None
    
    q = deque([(x, y)])
    visited = defaultdict(bool)

    
    cnt = 0
    while q:
        x, y = q.popleft()
        visited[(x, y)] = True
        cnt += 1
        
        for i in range(block_num):

            # 오른쪽
            if x+i < w and matrix[x+i][y] != 0 and not visited[(x+i, y)]:
                q.append((x+i, y))

            # 왼쪽
            if x-i >= 0 and matrix[x-i][y] != 0 and not visited[(x-i, y)]:
                q.append((x-i, y))

            # 위
            if matrix[x][y] != 0 and not visited[(x, y)]:
                q.append((x, y))

            # 아래
            if  y-1 >= 0 and matrix[x][y-1] != 0 and not visited[(x, y-1)]:
                q.append((x, y-1))

    for x, y in visited:
        if not visited[(x, y)]:
            continue
        matrix[x].pop(y)
        matrix[x].appned(0)
    
    return matrix, cnt

def find_num(arr):
    for i in range(h-1, -1, -1):
        if arr[i] > 0:
            return i
    return -1

def drop_ball(matrix, n, x, y, cnt = 0):
    if n == 0:
        global max_block
        max_block = max(max_block, cnt)
        return
    
    n_matrix, cnt_block = remove_block(deepcopy(matrix), x, y)
    if not n_matrix and not cnt_block:
        return
    cnt += cnt_block + 1

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
