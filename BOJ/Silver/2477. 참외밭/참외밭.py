n = int(input())
cur = (0, 0)
def next_point(cur, direct, dist):
    x, y = cur
    if direct == 1:
        return (x + dist, y)
    elif direct == 2:
        return (x - dist, y)
    elif direct == 3:
        return (x, y - dist)
    elif direct == 4:
        return (x, y + dist)

xs, ys, xys = [], [], []
for i in range(6):
    direct, dist = map(int, input().split())
    cur = next_point(cur, direct, dist)
    xs.append(cur[0])
    ys.append(cur[1])
    xys.append(cur)
    
xs.sort()
ys.sort()
xy_middle = (xs[2], ys[2])
area = 0
for xy in xys:
    area += abs(xy[0] - xy_middle[0]) * abs(xy[1] - xy_middle[1])
print(area * n)
    
