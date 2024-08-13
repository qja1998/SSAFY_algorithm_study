test_case = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def move(x, y, d_i):
    next_x, next_y = x + dx[d_i], y + dy[d_i]

    if 0 <= next_x < 4 and 0 <= next_y < 4:
        return next_x, next_y
    else:
        return None, None

def nums_search(matrix, x, y, result='', depth=0):
    if depth == 6:
        result += matrix[x][y]
        result_set.add(result)
        return

    result += matrix[x][y]
    for d_i in range(4):
        next_x, next_y = move(x, y, d_i)
        if next_x is not None:
            nums_search(matrix, next_x, next_y, result, depth + 1)


for t in range(test_case):
    matrix = [input().split() for _ in range(4)]

    result_set = set()

    for i in range(4):
        for j in range(4):
            nums_search(matrix, i, j)

    print(f"#{t + 1} {len(result_set)}")
