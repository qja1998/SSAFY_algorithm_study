# 원래 있던 곳으로 되돌아와야 함
# 대각선 이동
# 갔던 길 X
# 같은 숫자 X
# 최대 종류

# 상

from collections import defaultdict

dyx = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

test_case = int(input())

def calculate_path(x, y, dia_cnt, visitied, test_v):
    visitied_tmp = visitied[:]
    for i, cnt in enumerate(dia_cnt):
        for _ in range(cnt):
            
            dy, dx = dyx[i + 2]
            y, x = y + dy, x + dx
            if start_yx == (y, x):
                continue
            if cafe_matrix[y][x] in visitied_tmp:
                return False
            if not(0 <= y < n) or not(0 <= x < n):
                return False
            visitied_tmp += [cafe_matrix[y][x]]
            # test_v += [[x, y]]
            # print(visitied)
            # print(test_v)
    return True


def search_path(x, y, d_pre, menu_cnt=1, dia_cnt=[0, 0], visitied=[], test_v=[]):
    global max_cnt
    
    if d_pre == 1 and dia_cnt[0]*dia_cnt[1] != 0:
        # print(menu_cnt)
        # print(visitied)
        # print(test_v)
        
        # 바로 순회하며 계산
        if calculate_path(x, y, dia_cnt, visitied, test_v+[[x, y]]):
            max_cnt = max(max_cnt, (menu_cnt-1) * 2)
        #     print("max:", max_cnt)
        # print()
    
    for d in range(2):
        # 방향을 한 번 바꾼 경우 그 방향으로만 가야함
        if d_pre == 1 and d == 0:
            continue
        ny, nx = y + dyx[d][0], x + dyx[d][1]

        if not(0 <= ny < n) or not(0 <= nx < n):
            continue
        if cafe_matrix[ny][nx] in visitied:
            continue
        
        dia_tmp = dia_cnt[:]
        dia_tmp[d] += 1

        search_path(nx, ny, d, menu_cnt+1, dia_tmp, visitied+[cafe_matrix[ny][nx]], test_v+[[nx, ny]])

for t in range(test_case):
    n = int(input())

    cafe_matrix = [list(map(int, input().split())) for _ in range(n)]

    max_cnt = -1
    for y in range(n):
        for x in range(n):
            if (y == x or y+x == n-1) and (y == 0 or y == n-1):
                continue
            start_yx = (y, x)
            search_path(x, y, 0, visitied=[cafe_matrix[y][x]], test_v=[[x, y]])

    print(f"#{t+1} {max_cnt}")