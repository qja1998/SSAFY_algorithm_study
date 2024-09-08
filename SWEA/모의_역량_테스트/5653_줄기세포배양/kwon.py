from collections import deque

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

TC = int(input())

for t in range(1, TC+1):
    N, M, K = map(int, input().split())

    cells = {}
    for y in range(N):
        for x, v in enumerate(list(map(int, input().split()))):
            if v == 0:
                continue
            cells[(x, y)] = [v, v, v]

    active_q = deque()
    for time in range(K):
        # 비활성 시간이 끝나면 활성화 큐에 넣기
        for (x, y), (deactive, active, v) in cells.items():
            # 활성화 시간 끝나면 무시, 한 번 번식하면 무시
            if active != v:
                cells[(x, y)][1] -= 1
                continue
            if deactive == 0:
                active_q.append([[x, y], [active, v]])
            cells[(x, y)][0] -= 1

        # 번식 진행
        child_cell = {}
        while active_q:
            # 어차피 한 번 번식하면 이 위치는 쓸 일 없음
            [x, y], [active, v] = active_q.popleft()

            cells[(x, y)][1] -= 1
            
            for dx, dy in dxy:
                nxy = x + dx, y + dy
                # 이미 세포가 있는 곳은 무시
                if nxy in cells:
                    continue
                # 같은 곳으로 번식할 때
                if nxy in child_cell:
                    # 저장되어 있는 생명력이 높으면 스킵
                    if v < child_cell[nxy][1]:
                        continue
                child_cell[nxy] = [active-1, v]
        
        # 번식된 세포 cell로 옮겨주기
        for nxy, (active, v) in child_cell.items():
            cells[nxy] = [v, v, v]
        # breakpoint()

    result = 0
    for _, active, _ in cells.values():
        if active <= 0:
            continue
        result += 1

    print(f"#{t} {result}")


# 디버깅
def show_cell(cell_dict):
    xys = cell_dict.keys()
    max_x, min_x = max(xys, key=lambda x: x[0])[0], min(xys, key=lambda x: x[0])[0]
    max_y, min_y = max(xys, key=lambda x: x[1])[1], min(xys, key=lambda x: x[1])[1]

    show_matix = [[0]*(max_x-min_x+1) for _ in range(max_y-min_y+1)]
    for y in range(max_y-min_y+1):
        for x in range(max_x-min_x+1):
            if (x+min_x, y+min_y) not in cell_dict:
                continue
            show_matix[y][x] = cell_dict[(x+min_x, y+min_y)][-1]
    return show_matix