from collections import deque


def bfs(y, x):
    queue = deque([(y, x)])
    if y == end[0] and x == end[1]:
        return
    while queue:
        number = queue.popleft()
        y = number[0]
        x = number[1]
        for dy, dx in move:
            ny, nx = dy+y, dx+x
            if 0 <= ny < N and 0 <= nx < N:
                if chess_pan[ny][nx] == 0:
                    if (ny, nx) == (end[0], end[1]):
                        chess_pan[ny][nx] = chess_pan[y][x]+1
                        return
                    else:
                        chess_pan[ny][nx] = chess_pan[y][x]+1
                        queue.append((ny, nx))


T = int(input())

move = ((-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (-1, 2), (1, -2), (-1, -2))

for test_case in range(T):
    N = int(input())
    num = list(map(int, input().split()))
    start = (num[0], num[1])
    num = list(map(int, input().split()))
    end = (num[0], num[1])
    chess_pan = [[0] * N for _ in range(N)]
    bfs(start[0], start[1])

    print(chess_pan[end[0]][end[1]])
