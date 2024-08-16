# 원래 있던 곳으로 되돌아와야 함
# 대각선 이동
# 갔던 길 X
# 같은 숫자 X
# 최대 종류

# 상

from collections import defaultdict

dyx = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

test_case = int(input())

def calculate_path(x, y, dia_cnt, visitied):
    for i, cnt in enumerate(dia_cnt):
        for _ in range(cnt):
            if start_yx == (y, x):
                continue
            dy, dx = dyx[i + 2]
            y, x = y + dy, x + dx
            if cafe_matrix[y][x] in visitied:
                return False
            visitied += [cafe_matrix[y][x]]
    return True


def search_path(x, y, d, menu_cnt=0, dia_cnt=[0, 0], visitied=[]):
    global max_cnt
    print(visitied)
    if d >= 2:
        # 바로 순회하며 계산
        if calculate_path(x, y, dia_cnt, visitied):
            max_cnt = max(max_cnt, (menu_cnt-1) * 2)
            print(max_cnt)
        return
    
    ny, nx = y + dyx[d][0], x + dyx[d][1]

    if not(0 <= ny < n) or not(0 <= nx < n):
        return
    if cafe_matrix[ny][nx] in visitied:
        return
    
    dia_cnt[d] += 1
    # 직진
    search_path(nx, ny, d, menu_cnt+1, dia_cnt, visitied + [cafe_matrix[y][x]])
    # 꺾기
    search_path(nx, ny, d + 1, menu_cnt+1, dia_cnt,  visitied + [cafe_matrix[y][x]])

for t in range(test_case):
    n = int(input())

    cafe_matrix = [list(map(int, input().split())) for _ in range(n)]

    max_cnt = -1
    for y in range(n):
        for x in range(n):
            if (y == 0 and x == 0) or  (y == 0 and x == n-1) or (y == n-1 and  x == 0) or (y == n-1 and x == n-1):
                continue
            # visited_menu = defaultdict(bool)
            # visited_cafe = defaultdict(bool)
            start_yx = (x, y)
            search_path(x, y, 0)

    print(f"#{t+1} {max_cnt}")