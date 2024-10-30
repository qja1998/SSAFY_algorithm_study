from collections import deque, defaultdict

dxy = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dust_diffuse(dust, purifier, R, C):
    """
    1. 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
    (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
    인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
    확산되는 양은 A_{r,c}/5이고 소수점은 버린다. 즉, ⌊A_{r,c}/5⌋이다.
    (r, c)에 남은 미세먼지의 양은 A_{r,c} - ⌊A_{r,c}/5⌋×(확산된 방향의 개수) 이다.
    """

    diffuse = defaultdict(int)
    for x, y in dust:
        diffuse_dust = dust[(x, y)] // 5

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            # 비어있지 않음
            if (nx, ny) not in dust or dust[(nx, ny)] == 0 or (nx, ny) in purifier:
                continue
            
            # 범위 벗어남
            if not (0 <= nx < C and 0 <= ny < R):
                continue

            dust[(x, y)] -= diffuse_dust
            diffuse[(x, y)] += diffuse_dust

    for xy in diffuse:
        dust[xy] += diffuse[xy]


def do_purifier(purifier_up, purifier_down, dust, R, C):
    """
    2. 공기청정기가 작동한다.
    공기청정기에서는 바람이 나온다.
    위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
    바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
    공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
    """

    # 좌상우하 순으로 변경
    if (0, purifier_up[1]) in dust:
        left_down = dust[(0, purifier_up[1])]
    else:
        left_down = 0
    for y in range(purifier_up[1] + 1, -1, -1):
        if (0, y - 1) not in dust:
            continue
        dust[(0, y)] = dust[(0, y - 1)]
    dust[(0, 0)] = 0

    for x in range(0, C - 1):
        if (x + 1, 0) not in dust:
            continue
        dust[(x, 0)] = dust[(x + 1, 0)]
    dust[(C - 1, 0)] = 0

    for y in range(0, purifier_up[1] - 1):
        if (C, y + 1) not in dust:
            continue
        dust[(C, y)] = dust[(C, y + 1)]
    dust[(C - 1, purifier_up[1])] = 0

    for x in range(C - 2, -1, -1):
        if (x - 1, purifier_up[1]) not in dust:
            continue
        dust[(x, purifier_up[1])] = dust[(x - 1, purifier_up[1])]
    dust[(purifier_up[0] + 1, purifier_up[1])] = 0
    dust[(1, purifier_up[1])] = left_down


    if (0, purifier_down[1]) in dust:
        left_up = dust[(0, purifier_down[1])]
    else:
        left_up = 0
    
    for y in range(0, purifier_down[1] - 1):
        if (C, y + 1) not in dust:
            continue
        dust[(0, y)] = dust[(0, y + 1)]
    dust[(0, R)] = 0

    for x in range(0, R - 1):
        if (x + 1, R) not in dust:
            continue
        dust[(x, R)] = dust[(x + 1, R)]
    dust[(C - 1, R - 1)] = 0

    for y in range(purifier_down[1] + 1, -1, -1):
        if (C, y - 1) not in dust:
            continue
        dust[(C, y)] = dust[(C, y - 1)]
    dust[(C - 1, purifier_down[1])] = 0

    for x in range(C - 2, -1, -1):
        if (x, purifier_down[1]) in purifier:
            continue
        if (x - 1, purifier_down[1]) not in dust:
            continue
        dust[(x, purifier_down[1])] = dust[(x - 1, purifier_down[1])]
    dust[(purifier_down[0] + 1, purifier_down[1])] = 0
    dust[(1, purifier_down[1])] = left_up
    


R, C, T = map(int, input().split())

dust = {}
purifier = []

for y in range(R):
    for x, val in enumerate(map(int, input().split())):
        if val > 0:
            dust[(x, y)] = val
        elif val == -1:
            purifier.append((x, y))

purifier_up = purifier[0]
purifier_down = purifier[1]

for _ in range(T):
    dust_diffuse(dust, purifier, R, C)
    do_purifier(purifier_up, purifier_down, dust, R, C)

result = 0
for xy in dust:
    result += dust[xy]

print(result)