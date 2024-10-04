from collections import defaultdict

N, M, D = map(int, input().split())

enermy = defaultdict(int)

for y in range(N):
    for x, value in enumerate(map(int, input().split())):
        enermy[(x, y)] = value


def shot(a):
    x, y = a
    for i in range(-D, D+1):
        chk_x, chk_y_range = x + i, range(y-D+abs(i)+1, y+D-abs(i)+1)
        for chk_y in chk_y_range:


def step(archer):
    for a in archer:
        shot(a)