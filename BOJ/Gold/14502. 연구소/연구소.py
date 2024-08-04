n, m = map(int, input().split()) # 세로, 가로

lab = []
for _ in range(n):
    lab.append(list(map(int, input().split())))

# walls position : 

def isntall_walls(lab, positions):
    for x, y in positions:
        lab[y][x] = 1
    return lab

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

virus_pos = []

for y in range(n):
    for x in range(m):
        if lab[y][x] == 2:
            virus_pos.append((x, y))


def check_virus(lab, x, y):

    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if (0 <= next_x < m) and (0 <= next_y < n):
            if lab[next_y][next_x] == 0:
                lab[next_y][next_x] = 2
                lab = check_virus(lab, next_x, next_y)

    return lab


max_safe_zone = 0

for wall1 in range(n * m - 2):
    xy1 = (wall1 % m, wall1 // m)
    if lab[xy1[1]][xy1[0]] != 0:
        continue
    for wall2 in range(wall1 + 1, n * m - 1):
        xy2 = (wall2 % m, wall2 // m)
        if lab[xy2[1]][xy2[0]] != 0:
            continue
        for wall3 in range(wall2 + 1, n * m):
            xy3 = (wall3 % m, wall3 // m)
            if lab[xy3[1]][xy3[0]] != 0:
                continue

            installed_lab = isntall_walls([l.copy() for l in lab], [xy1, xy2, xy3])
            
            safe_zone = 0
            for x, y in virus_pos:
                installed_lab = check_virus(installed_lab, x, y)
            
            for y in range(n):
                for x in range(m):
                    if installed_lab[y][x] == 0:
                        safe_zone += 1

            max_safe_zone = max(safe_zone, max_safe_zone)

print(max_safe_zone)