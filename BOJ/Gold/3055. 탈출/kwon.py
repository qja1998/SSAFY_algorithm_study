from collections import deque

def show(matrix, visited):
    for r, c in visited:
        matrix[r][c] = 'v'
    return matrix

R, C  = map(int, input().split())

matrix = [list(input()) for _ in range(R)]

drc = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def water(matrix):
    n_water = set()
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == '*':
                for dr, dc in drc:
                    nr, nc = r + dr, c + dc
                    if not(0 <= nr < R and 0 <= nc < C):
                        continue
                    if matrix[nr][nc] != '.':
                        continue
                    n_water.add((nr, nc))
    
    for r, c in list(n_water):
        matrix[r][c] = '*'
    return matrix

def search(matrix):
    q = deque([[sr, sc, 0]])
    visited = [[sr, sc]]
    pre_time = 0
    while q:
        r, c, time = q.popleft()
        if pre_time == time:
            matrix = water(matrix)
            pre_time += 1

        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if not(0 <= nr < R and 0 <= nc < C):
                continue
            if [nr, nc] in visited:
                continue
            if matrix[nr][nc] == 'D':
                return time + 1
            if matrix[nr][nc] != '.':
                continue

            visited.append([nr, nc])
            q.append([nr, nc, time + 1])
    return False

# 필요한 최소 시간 
for r in range(R):
    for c in range(C):
        if matrix[r][c] == 'S':
            sr = r
            sc = c

time = search(matrix.copy())
if time:
    print(time)
else:
    print('KAKTUS')