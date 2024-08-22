# 상하좌우
from collections import defaultdict

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