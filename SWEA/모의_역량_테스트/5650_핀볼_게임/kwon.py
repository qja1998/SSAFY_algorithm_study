from collections import defaultdict

# 하 상 우 좌
dyx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def init_dict():
    return [0, 0]

# 일자 벽에 부딪힐 때
def _simple_bounce(d):
    if d % 2 == 0:
        d += 1
    else:
        d -= 1
    return False

# 벽에 부딪힐 때
def bounce(wall, d):
    if wall == 1:
        if d == 0 or d == 3:
            d = (d+2) % 4
        else:
            d = _simple_bounce(d)
    elif wall == 2:
        if d == 1 or d == 3:
            d = (d+1) % 4
        else:
            d = _simple_bounce(d)
    elif wall == 3:
        if d == 1 or d == 2:
            d = (d+2) % 4
        else:
            d = _simple_bounce(d)
    elif wall == 4:
        if d == 0 or d == 2:
            d = (d+1) % 4
        else:
            d = _simple_bounce(d)
    elif wall == 5:
        d = _simple_bounce(d)

    return d

# 웜홀
def wormhall(wormhall, y, x):
    y_sum, x_sum = wormhall_dict[wormhall]
    ny = y_sum - y
    nx = x_sum - x
    return ny, nx

def pin_ball(y, x, d, start_yx, score=0):
    print(y, x, d)

    while True:
        global max_score
        ny, nx = y + dyx[d][0], x + dyx[d][1]

        # 범위 벗어나는 경우
        if not(0 <= ny < n+1) or not(0 <= nx < n+1):
            return
        
        visited[(y, x, d)] = True
        
        next_pos = pin_ball_map[ny][nx]
        
        if next_pos == 0:
            y, x, d = ny, nx, d
        elif 1 <= next_pos <= 5:
            # 벽
            nd = bounce(next_pos, d)
            if not nd:
                max_score = max(max_score, 2*score+1)
                return
            
            y, x, d, score = ny, nx, nd, score+1

        elif 6 <= next_pos <= 10:
            # 웜홀
            ny, nx = wormhall(next_pos, ny, nx)
            y, x, score = ny, nx, score+1

        elif next_pos == -1 or (ny, nx) == start_yx:
            # 블랙홀, 도착지점
            max_score = max(max_score, score)
            return

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

    # # 위치에서의 최대 점수 / 안될듯?
    # memo = []

    # (위치, 방향) : 방문 체크
    visited = defaultdict(bool)

    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if pin_ball_map[y][x] != 0:
                continue
            for d in range(4):
                if visited[(y, x, d)]:
                    continue
                start_yx = (y, x)
                pin_ball(y, x, d, start_yx)

    print(f"#{t+1} {max_score}")