from collections import defaultdict


test_case = int(input())

def init_position(germs):
    position_list = []
    for y, x, num, d in germs:
        # 미생물 수, 방향, 이동한 횟수
        matrix[y, x].append([num, d - 1, False])
        position_list.append([y, x])
    return position_list

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def move(y, x, d):
    ny, nx = y + dy[d], x + dx[d]
    if not (0 <= ny < n and 0 <= nx < n):
        return None, None
    return ny, nx

for t in range(test_case):
    # n * n, m 시간, k개 군집
    n, m, k = map(int, input().split())

    # 세로, 가로 위치, 미생물 수, 이동 방향(상, 하, 좌, 우)
    germs = [list(map(int, input().split())) for _ in range(k)]

    matrix = defaultdict(list)
    max_dict = defaultdict(int)

    position_list = init_position(germs)

    for _ in range(m):
        yxs = list(matrix.keys())
        for y, x in yxs:
            for pos in matrix[y, x]:
                if not pos:
                    continue
                origin_pos = pos
                num, d, is_move = pos
                # 이미 움직인 경우 스킵
                if is_move:
                    continue
                if num == 0:
                    continue
                
                ny, nx = move(y, x, d)
                if ny == None:
                    continue

                
                # 약품 처리(0 - 1, 2 - 3)
                if ny == 0 or ny == n - 1 or nx == 0 or nx == n -1:
                    num = num // 2
                    d = d + 1 if d % 2 == 0 else d - 1

                matrix[ny, nx].append([num, d, True])
                matrix[y, x].remove(origin_pos)


        del_pos = []
        for y, x in matrix:
            if not matrix[y, x]:
                del_pos.append((y, x))
                continue
            max_num = 0
            max_d = 0
            sum_num = 0
            for i, (num, d, is_move) in enumerate(matrix[y, x]):
                # 병합 처리
                if num > max_num:
                    max_num = num
                    max_d = d
                
                sum_num += num
            if max_num == 0:
                del_pos.append((y, x))
                continue
            matrix[y, x] = [[sum_num, max_d, False]]
        
        for y, x in del_pos:
            del matrix[y, x]

    result = 0
    for pos in matrix.values():
        result += pos[0][0]
    print(f"#{t + 1} {result}")