from collections import defaultdict, deque

dxy = [[-1, 0], [0, -1], [1, 0]]

N, M, D = map(int, input().split())

enermy = []

enermy_n = 0
for y in range(N):
    for x, value in enumerate(map(int, input().split())):
        enermy.append([x, y])
        enermy_n += 1


def shot(archer):
    q = deque([archer, 0])
    visited = [archer]

    while q:
        (c_x, c_y), cnt = q.popleft()

        if cnt >= D:
            continue
        if [c_x, c_y] in enermy:
            return c_x, c_y
        for dx, dy in dxy:
            nx, ny = c_x + dx, c_y + dy
            
            if not(0 <= nx < M and 0 <= ny < N):
                continue

            q.append((nx, ny), cnt+1)
            visited.append((nx, ny))
        
    return False

def step(archers, enermy_cnt=0):
    global max_enermy
    if enermy_n == enermy_cnt:
        max_enermy = max(max_enermy, enermy_cnt)
        return
    for i, archer in enumerate(archers):
        shoted_enermy = shot(archer)
        if shoted_enermy:
            enermy[shoted_enermy] = False
            enermy_cnt += 1

        for e in enermy:
            if enermy[e]:
                enermy[e] = False
                e = list(e)
                e[1] += 1
                if e[1] == N:
                    enermy_cnt += 1s
                    continue
                enermy[tuple(e)] = True

        step(archers[i:], enermy_cnt)

        if shoted_enermy:
            enermy[shoted_enermy] = True
            enermy_cnt -= 1

max_enermy = 0