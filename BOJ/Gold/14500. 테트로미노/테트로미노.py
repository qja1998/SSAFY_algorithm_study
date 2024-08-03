n, m = map(int, input().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

# 0: 우, 1: 좌, 2: 상, 3: 하
x_dir = [1, -1, 0, 0]
y_dir = [0, 0, -1, 1]

# 블록 형태 : x 시작 - 끝,  y 시작 - 끝, ㅜ 모양 판별
tetromino_dict = {(0, 3, 1) : ((0, m - 1), (0, n - 1), False),
             
             (0, 0, 0) : ((0, m - 3), (0, n), False),
             (3, 3, 3) : ((0, m), (0, n - 3), False),

             (3, 0, 3) : ((0, m - 1), (0, n - 2), False),
             (0, 2 ,0) : ((0, m - 2), (1, n), False),
             (2, 0, 2) : ((0, m - 1), (2, n), False),
             (0, 3, 0) : ((0, m - 2), (0, n - 1), False),

             (3, 3, 0) : ((0, m - 1), (0, n - 2), False),
             (2, 0, 0) : ((0, m - 2), (1, n), False),
             (0, 3, 3) : ((0, m - 1), (0, n - 2), False),
             (0, 0, 2) : ((0, m - 2), (1, n), False),
             (0, 2, 2) : ((0, m - 1), (2, n), False),
             (3, 0, 0) : ((0, m - 2), (0, n - 1), False),
             (2, 2, 0) : ((0, m - 1), (2, n), False),
             (0, 0, 3) : ((0, m - 2), (0, n - 1), False),
            
            # ㅜ 모양은 중간에서 시작
             (1, 3, 0) : ((1, m - 1), (0, n - 1), True),
             (2, 1, 3) : ((1, m), (1, n - 1), True),
             (1, 2, 0) : ((1, m - 1), (1, n), True),
             (2, 0, 3) : ((0, m - 1), (1, n - 1), True)}

def sum_num(tetromino, x_start, x_end, y_start, y_end, is_T_shape=False, paper = paper):
    max_sum = 0

    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            block_sum = 0
            block_sum += paper[y][x]
            tmp_x, tmp_y = x, y
            if not is_T_shape:
                for block in tetromino:
                    tmp_x += x_dir[block]
                    tmp_y += y_dir[block]
                    block_sum += paper[tmp_y][tmp_x]
            else:
                for block in tetromino:
                    tmp_x = x + x_dir[block]
                    tmp_y = y + y_dir[block]
                    block_sum += paper[tmp_y][tmp_x]
            max_sum = max(max_sum, block_sum)

    return max_sum

max_sum = 0

for tetromino in tetromino_dict:
    (x_start, x_end), (y_start, y_end), is_sep = tetromino_dict[tetromino]
    max_sum = max(max_sum, sum_num(tetromino, x_start, x_end, y_start, y_end, is_sep))

print(max_sum)