from collections import defaultdict

test_case = int(input())

dyx = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# 전선 연결시 횟수 return
def connect(y, x, d):
    cnt = 0
    while True:
        y, x = y + dyx[d][0], x + dyx[d][1]
        if not (0 <= y < n and 0 <= x < n):
            break
        if board[y][x] != 0:
            return 0
        cnt += 1

    return cnt


# 전선에 맞게 맵을 변경
def change_board(y, x, connect_cnt, d, reverse=False):
    dy, dx = dyx[d]
    if dx == 0:
        for y_i in range(y + dy, y + dy * (connect_cnt + 1), dy):
            if reverse:
                board[y_i][x] = 0
                continue
            board[y_i][x] = 2
    elif dy == 0:
        for x_i in range(x + dx, x + dx * (connect_cnt + 1), dx):
            if reverse:
                board[y][x_i] = 0
                continue
            board[y][x_i] = 2


def dfs(connected_cnt=0, total_line_cnt=0, depth=0):
    global max_connection, min_line
    # # 지금까지 연결된 개수가 작은데 라인은 더 많이 쓴 경우
    # if connected_cnt < max_connection and total_line_cnt >= min_line:
    #     return

    # core를 모두 탐색한 경우
    if core_num == depth:
        # 연결한 개수가 최대 개수랑 같으면 최소 라인 수만 갱신
        if max_connection == connected_cnt:
            min_line = min(min_line, total_line_cnt)
        # 연결한 개수가 가장 크다면 무조건 갱신
        elif max_connection < connected_cnt:
            max_connection = connected_cnt
            min_line = total_line_cnt
        return

    y, x = cores[depth]
    for d in range(4):
        line_cnt = connect(y, x, d)
        if line_cnt:
            change_board(y, x, line_cnt, d)
        # 연결할 수 없는 경우 방향이 달라도 같은 결과를 보임 -> 방문 확인
        else:
            if visited[connected_cnt, total_line_cnt, depth, line_cnt]:
                continue
            visited[connected_cnt, total_line_cnt, depth, line_cnt] = True

        dfs(connected_cnt + bool(line_cnt), total_line_cnt + line_cnt, depth + 1)
        if line_cnt:
            change_board(y, x, line_cnt, d, True)


for t in range(test_case):
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]

    cores = []

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if board[i][j] == 0:
                continue
            cores.append((i, j))

    core_num = len(cores)
    max_connection = 0
    min_line = 13
    visited = defaultdict(bool)

    dfs()

    print(f"#{t + 1} {min_line}")
