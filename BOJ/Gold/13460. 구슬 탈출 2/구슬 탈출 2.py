import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test", action='store')
args = parser.parse_args()

n, m  = map(int, input().split())
o, r, b = (-1, ), (-1, ), (-1, )
map_list = []
for i in range(n):
    row = input()
    if o[0] == -1:
        o = (row.find('O'), i)
    if r[0] == -1:
        r = (row.find('R'), i)
    if b[0] == -1:
        b = (row.find('B'), i)
   
    map_list.append(list(row))

def tilt(map_list, dir, r, b):
    rx, ry = r
    bx, by = b
    dir_x, dir_y = dir
    if dir_x != 0:
        if dir_x * rx > dir_x * bx: late = 'b'
        else: late = 'r'
    else:
        if dir_y * ry > dir_y * by: late = 'b'
        else: late = 'r'
    
    cur_r = map_list[ry][rx]
    cur_b = map_list[by][bx]
    
    next_r, next_b = '.', '.'
    
    while (next_r != '#' and cur_r != 'O') or (next_b != '#'):
        next_r = map_list[ry + dir_y][rx + dir_x]
        next_b = map_list[by + dir_y][bx + dir_x]
        if next_r != '#' and cur_r != 'O':
            cur_r = next_r
            rx += dir_x
            ry += dir_y
        if next_b != '#':
            cur_b = next_b
            bx += dir_x
            by += dir_y
        if cur_b == 'O':
            return -1, -1, -1, -1

    if (rx, ry) == (bx, by):
        if late == 'b':
            bx -= dir_x
            by -= dir_y
        else:
            rx -= dir_x
            ry -= dir_y
        
    return rx, ry, bx, by
        
def move(dir, r, b):
    m_rx, m_ry, m_bx, m_by = tilt(map_list, dir, r, b)
    if m_rx == -1: return (-1, -1)
    elif (m_rx, m_ry) == o: return (True, True)
    else:
        r, b = (m_rx, m_ry), (m_bx, m_by)
        return r, b
        
visited = [[[[0] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

def sim(r, b):
    q = []
    q.append((r, b, None))
    
    while q:
        cur_r, cur_b, pre_d = q.pop(0)
        dirs = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        pre_cnt = visited[cur_r[1]][cur_r[0]][cur_b[1]][cur_b[0]]
        
        if pre_d:
            dirs.remove(pre_d)
            dirs.remove((-pre_d[0], -pre_d[1]))
            
        for d in dirs:
            r_tmp, b_tmp = move(d, cur_r, cur_b)
            if r_tmp == -1:
                continue
            elif r_tmp == True:
                return pre_cnt + 1
            elif pre_cnt >= 10:
                return -1
            elif not visited[r_tmp[1]][r_tmp[0]][b_tmp[1]][b_tmp[0]]:  # 방문 안함
                q.append((r_tmp, b_tmp, d))
                visited[r_tmp[1]][r_tmp[0]][b_tmp[1]][b_tmp[0]] = pre_cnt + 1
        
    return -1

print(sim(r, b))