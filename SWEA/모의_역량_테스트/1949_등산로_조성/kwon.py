from copy import deepcopy

test_case = int(input())

dyx = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def search_path(mountain, y, x, visited, length=1, use_k=False):
    global max_length
    cur_h = mountain[y][x]
    tmp_mountain = deepcopy(mountain)
    for dy, dx in dyx:
        ny, nx = y + dy, x + dx
        if not(0 <= ny < n) or not(0 <= nx < n):
            continue
        if (ny, nx, use_k) in visited:
            max_length = max(max_length, length)
            continue

        n_h = mountain[ny][nx]
        if cur_h <= n_h:
            if use_k:
                max_length = max(max_length, length)
                continue
            # 깎을 수 있으면, 높이 차이보다 하나 더 깎기 (최소로 깎기)
            # 깎아도 안되면 갱신 후 넘기기
            if k <= n_h - cur_h:
                max_length = max(max_length, length)
                continue
            for k_i in (n_h-cur_h+1, k+1):
                tmp_mountain[ny][nx] -= k_i
                search_path(tmp_mountain, ny, nx, visited+[(ny, nx, use_k)], length+1, True)
                tmp_mountain[ny][nx] += k_i
            continue
        
        search_path(tmp_mountain, ny, nx, visited+[(ny, nx, use_k)], length+1, use_k)

for t in range(test_case):
    n, k = map(int, input().split())

    mountain = [list(map(int, input().split())) for _ in range(n)]

    top_list = []
    max_h = 0
    # 가장 높은 곳(시작점) 찾기
    for y in range(n):
        for x in range(n):
            if mountain[y][x] > max_h:
                max_h = mountain[y][x]
                top_list = [(y, x)]
            elif mountain[y][x] == max_h:
                top_list.append((y, x))
    
    max_length = 0
    for y, x in top_list:
        search_path(mountain, y, x, [(y, x, False)])

    print(f"#{t+1} {max_length}")





#1 6
#2 3
#3 6 7
#4 4
#5 2
#6 12
#7 5
#8 7
#9 10
#10 19