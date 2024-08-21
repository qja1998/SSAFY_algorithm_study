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

# # 일자 벽에 부딪힐 때
# def _simple_bounce(d):
#     if d % 2 == 0:
#         d += 1
#     else:
#         d -= 1
#     return -1

# # 벽에 부딪힐 때
# def bounce(wall, d):
#     if wall == 1:
#         if d == 0 or d == 3:
#             d = (d+2) % 4
#         else:
#             d = _simple_bounce(d)
#     elif wall == 2:
#         if d == 1 or d == 3:
#             d = (d+1) % 4
#         else:
#             d = _simple_bounce(d)
#     elif wall == 3:
#         if d == 1 or d == 2:
#             d = (d+2) % 4
#         else:
#             d = _simple_bounce(d)
#     elif wall == 4:
#         if d == 0 or d == 2:
#             d = (d+3) % 4
#         else:
#             d = _simple_bounce(d)
#     elif wall == 5:
#         d = _simple_bounce(d)

#     return d

# 웜홀
def wormhall(wormhall, y, x):
    y_sum, x_sum = wormhall_dict[wormhall]
    ny = y_sum - y
    nx = x_sum - x
    return ny, nx

def pin_ball(y, x, d, start_yx):
    score = 0

    while True:
        global max_score
        y, x = y + dyx[d][0], x + dyx[d][1]

        # 범위 벗어나는 경우
        if not(0 <= y < n+1) or not(0 <= x < n+1):
            return
        
        next_pos = pin_ball_map[y][x]
        
        if next_pos == -1 or (y, x) == start_yx:
            # 블랙홀, 도착지점
            max_score = max(max_score, score)
            return
        # elif next_pos == 0:
        #     y, x = y, x
        elif 1 <= next_pos <= 5:
            # 벽
            nd = change_dir[pin_ball_map[y][x]][d]
            # if back_dir[(d, nd)]:
            #     max_score = max(max_score, 2*score+1)
            #     return
            
            d, score = nd, score+1

        elif 6 <= next_pos <= 10:
            # 웜홀
            y, x = wormhall(next_pos, y, x)

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
                pin_ball(y, x, d, (y, x))
    print(f"#{t+1} {max_score}")


'''
# 상하좌우
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

# 블록별 방향 바꾸기
change_dir = ((),
              (1, 3, 0, 2),
              (3, 0, 1, 2),
              (2, 0, 3, 1),
              (1, 2, 3, 0),
              (1, 0, 3, 2))

# 게임 시작 위치와 방향 넘기면 게임 횟수 리턴
def play_game(r, c, d):
    global wormhole_info
    score = 0
    sr, sc = r, c       # 시작 위치 저장
    while True:
        r += dr[d]      # 이동하면서 시작해야 함
        c += dc[d]
        # 출발 위치로 돌아오거나 블랙홀 만나면 게임 끝. 점수 리턴
        if (r, c) == (sr, sc) or A[r][c] == -1:
            return score
        if 1 <= A[r][c] <= 5:           # 블록 만나면 방향 바꾸고 점수 + 1
            d = change_dir[A[r][c]][d]
            score += 1
        elif 6 <= A[r][c] <= 10:        # 웜홀 만나면 같은 번호의 웜홀로 이동. 방향은 유지
            r, c = wormhole_info[(r, c)]

# main
T = int(input())
for tc in range(T):
    N = int(input())
    wormhole_check = [0] * 11
    wormhole_info = dict()      # 웜홀 쌍 정보
    A = [[5] * (N+2)]   # 맵 벽(5)으로 둘러싸기
    for i in range(1, N+1):
        A.append([5] + list(map(int, input().split())) + [5])
        for j in range(1, N+1):
            if 6 <= A[i][j] <= 10:
                num = A[i][j]
                if not wormhole_check[num]:
                    wormhole_check[num] = (i, j)
                else:   # 같은 번호 웜홀끼리 위치 정보 저장
                    wormhole_info[wormhole_check[num]] = (i, j)
                    wormhole_info[(i, j)] = wormhole_check[num]
    A.append([5] * (N+2))

    # 게임 시작
    MAX = float('-inf')  # 게임에서 얻을 수 있는 최대 점수
    for sr in range(1, N+1):
        for sc in range(1, N+1):
            if A[sr][sc] == 0:      # 시작 위치와 방향 정한 후 게임 start
                for sd in range(4):
                    MAX = max(MAX, play_game(sr, sc, sd))
    print("#{} {}".format(tc+1, MAX))

'''