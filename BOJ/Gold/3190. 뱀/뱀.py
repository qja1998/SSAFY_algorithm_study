import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
k = int(input())

apples = defaultdict(list)
for i in range(k):
    x, y = list(map(int, input().split()))
    apples[y - 1].append(x - 1)

l = int(input())

moves = {}
for i in range(l):
    t, d = input().split()
    moves[int(t)] = d

snake = [[0, 0]]

# L이 왼쪽. D가 오른쪽

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]
dir_idx = 0

def move(x, y, dir_idx):
    next_x = x + dir_x[dir_idx]
    next_y = y + dir_y[dir_idx]

    try:
        if next_y in apples[next_x]:
            snake.append([next_x, next_y])
            apples[next_x].remove(next_y)
        elif [next_x, next_y] in snake or not (0 <= next_x < n) or not (0 <= next_y < n):
            return [-1, -1]
        else:
            snake.append([next_x, next_y])
            snake.pop(0)
    except:
        if [next_x, next_y] in snake or not (0 <= next_x < n) or not (0 <= next_y < n):
            return [-1, -1]
        else:
            snake.append([next_x, next_y])
            snake.pop(0)
    
    return next_x, next_y

cnt = 0
x, y = 0, 0

while True:
    if cnt in moves:
        if moves[cnt] == 'L':
            dir_idx = (dir_idx + 4 - 1) % 4
        else:
            dir_idx = (dir_idx + 1) % 4

    x, y = move(x, y, dir_idx)
    cnt += 1
    if [x, y] == [-1, -1]:
        break

print(cnt)