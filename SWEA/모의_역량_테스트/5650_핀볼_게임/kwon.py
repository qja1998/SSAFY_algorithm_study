# code 1

from collections import defaultdict

dyx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

change_dir = ((),
              (2, 0, 3, 1),
              (1, 2, 3, 0),
              (1, 3, 0, 2),
              (3, 0, 1, 2),
              (1, 0, 3, 2))

back_dir = defaultdict(bool)
back_dir[(0, 1)] = True
back_dir[(1, 0)] = True
back_dir[(2, 3)] = True
back_dir[(3, 2)] = True

def init_dict():
    return [0, 0]

# 웜홀
def wormhall(wormhall, y, x):
    y_sum, x_sum = wormhall_dict[wormhall]
    ny = y_sum - y
    nx = x_sum - x
    return ny, nx

def pin_ball(y, x, d):
    score = 0
    start_yx = (y, x)

    while True:
        y, x = y + dyx[d][0], x + dyx[d][1]

        # 범위 벗어나는 경우
        if not(0 <= y < n+2) or not(0 <= x < n+2):
            print(y, x)
            return
        
        cur_pos = pin_ball_map[y][x]
        
        if cur_pos == -1 or (y, x) == start_yx:
            # 블랙홀, 도착지점
            return score
        
        if 1 <= cur_pos <= 5:
            # 벽
            nd = change_dir[pin_ball_map[y][x]][d]
            if back_dir[(d, nd)]:
                return 2*score+1
            d, score = nd, score+1

        elif 6 <= cur_pos <= 10:
            # 웜홀
            y, x = wormhall(cur_pos, y, x)

test_case = int(input())

for t in range(test_case):
    n = int(input())

    # map을 받되 주변을 벽으로 둘러쌈
    pin_ball_map = [[5] + list(map(int, input().split())) + [5] for _ in range(n)]
    pin_ball_map = [[5]*(n+2)] + pin_ball_map + [[5]*(n+2)]

    wormhall_dict = defaultdict(init_dict)
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            cur = pin_ball_map[y][x]
            if 6 <= cur <= 10:
                wormhall_dict[cur][0] += y
                wormhall_dict[cur][1] += x

    max_score = 0

    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if pin_ball_map[y][x] != 0:
                continue
            for d in range(4):
                max_score = max(max_score, pin_ball(y, x, d))
    print(f"#{t+1} {max_score}")