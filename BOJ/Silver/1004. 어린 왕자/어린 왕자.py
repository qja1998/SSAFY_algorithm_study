t = int(input())
for _ in range(t):
    cnt = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for _ in range(n):
        c_x, c_y, r = map(int, input().split())
        r = r ** 2
        dis1 = (c_x - x1) ** 2 + (c_y - y1) ** 2
        dis2 = (c_x - x2) ** 2 + (c_y - y2) ** 2
        if (dis1 < r and dis2 < r) or (dis1 > r and dis2 > r):
            continue
        else:
            cnt += 1
    print(cnt)