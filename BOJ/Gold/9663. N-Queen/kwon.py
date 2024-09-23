from collections import defaultdict
from copy import deepcopy

N = int(input())

def chk_path(chess, y):
    for i in range(y):
        if chess[y] == chess[i] or (abs(chess[y]-chess[i]) == abs(y-i)):
            return False
    return True

def n_queen(chess, y=0):
    global cnt
    if y == N:
        cnt += 1
        return
    
    for nx in range(N):
        chess[y] = nx
        if chk_path(chess, y):
            n_queen(chess, y+1)


chess = [0] * N
cnt = 0

n_queen(chess)
print(cnt)