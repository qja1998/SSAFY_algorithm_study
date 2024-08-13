dx = [1, -1]

# 가야할 위치 확인
def chk_direction(ladder, x, y):
    for i in range(2):
        next_x = x + dx[i]
        if 0 <= next_x < 100:
            if ladder[y][next_x] == 1:
                return dx[i]
    return 0


# 실제로 움직이기
def mov_ladder(ladder, x, y=0):
    # y가 끝에 도달하면 멈춤
    while y < 99:
        d = chk_direction(ladder, x, y)
        # print(d)
        if d == 0:
            y += 1
        else:
            x += d
            while ladder[y + 1][x] == 0:
                x += d
            y += 1
    # 마지막 값 반환
    return ladder[y][x]


for _ in range(10):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i, x in enumerate(ladder[0]):
        if x == 1:
            if mov_ladder(ladder, i) == 2:
                print(f'#{t} {i}')
                break