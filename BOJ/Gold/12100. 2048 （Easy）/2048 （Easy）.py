import sys
input = sys.stdin.readline

n = int(input())
num_map = [list(map(int, input().split())) for _ in range(n)]

max_list = []
for row in num_map:
    max_list.append(max(row))

max_num = max(max_list)
dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]

def move(num_map, dir_i):
    global max_num
    dx, dy = dir_x[dir_i], dir_y[dir_i]
    
    if dx != 0:
        for y in range(n):
            is_sum = False
            pre = -1
            for i in range(0, n)[::-dx]:
                if num_map[y][i] == 0:
                    if pre == -1:
                        pre = 0
                        pre_idx = i + dx
                    continue
                cur = num_map[y][i]
                if pre == -1:
                    pre = cur
                    pre_idx = i
                elif cur != pre or is_sum:
                    if pre_idx - dx != i: # 수가 다르고 움직일 수 있는 경우
                        num_map[y][pre_idx - dx] = cur
                        num_map[y][i] = 0
                    pre_idx = pre_idx - dx
                    pre = cur
                    is_sum = False
                else: # 수가 같아서 합쳐지는 경우
                    num_map[y][pre_idx] += cur
                    pre = num_map[y][pre_idx]
                    if pre > max_num:
                        max_num = pre
                    num_map[y][i] = 0
                    is_sum = True

    elif dy != 0:
        for x in range(n):
            is_sum = False
            pre = -1
            for i in range(0, n)[::-dy]:
                if num_map[i][x] == 0:
                    if pre == -1:
                        pre = 0
                        pre_idx = i + dy
                    continue
                cur = num_map[i][x]
                if pre == -1:
                    pre = cur
                    pre_idx = i
                elif cur != pre or is_sum:
                    if pre_idx - dy != i:
                        num_map[pre_idx - dy][x] = cur
                        num_map[i][x] = 0
                    pre_idx = pre_idx - dy
                    pre = cur
                    is_sum = False
                    
                else:
                    num_map[pre_idx][x] += cur
                    pre = num_map[pre_idx][x]
                    if pre > max_num:
                        max_num = pre
                    num_map[i][x] = 0
                    is_sum = True
    
    return num_map

def brute_force(num_map, depth = 0):
    if depth == 5:
        return
    
    for i in range(4):
        num_map_new = move([row[:] for row in num_map], i)
        if num_map != num_map_new:
            brute_force(num_map_new, depth + 1)
            
brute_force(num_map)
print(max_num)