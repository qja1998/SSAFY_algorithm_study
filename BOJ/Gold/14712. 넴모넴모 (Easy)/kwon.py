from collections import defaultdict

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]
chk_dxy1 = [(-1, 0), (0, -1), (-1, -1)]
chk_dxy2 = [(1, 0), (0, -1), (1, -1)]

def show_nemo(visited):
    matrix = [[0]*N for _ in range(M)]

    for (x, y), v in visited.items():
        if v:
            matrix[y][x] = 1
    return matrix
        

# 사각형이 완성되는지 확인(완성되면 True)
def chk_nemo(x, y, installed):
    chk_cnt1 = 0
    for dx, dy in chk_dxy1:
        nx, ny = x+dx, y+dy
        if installed[(nx, ny)]:
            chk_cnt1 += 1

    chk_cnt2 = 0
    for dx, dy in chk_dxy2:
        nx, ny = x+dx, y+dy
        if installed[(nx, ny)]:
            chk_cnt2 += 1

    print(x, y)
    print('cnt', chk_cnt1, chk_cnt2)
    
    return chk_cnt1 == 3 or chk_cnt2 == 3

def fill_nemo(x, y, installed, visited):
    global cnt
    if x >= N-1 and y >= M-1:
        # for row in show_nemo(visited):
        #     print(row)
        # print()
        cnt += 1
        return
    
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        # 범위 벗어날 때
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if visited[(nx, ny)]:
            continue

        visited[(nx, ny)] = True
        # 사각형이 완성 안되는 경우
        if not chk_nemo(nx, ny, installed):
            # 다음 위치에 네모 생성
            installed[(nx, ny)] = True
            fill_nemo(nx, ny, installed, visited)
        
        # 다음 위치에 네모 생성 X
        installed[(nx, ny)] = False
        fill_nemo(nx, ny, installed, visited)

        visited[(nx, ny)] = False

N, M = map(int, input().split())

installed = defaultdict(bool)
visited = defaultdict(bool)

visited[(0, 0)] = True

cnt = 0
# 시작점에 넴모 놓지 않을 때
fill_nemo(0, 0, installed, visited)

installed[(0, 0)] = True
# 시작점에 넴모 놓을 때
fill_nemo(0, 0, installed, visited)

print(cnt)