# import sys
# sys.stdin = open("sample_input.txt", 'r')

from collections import deque

# 사방 탐색
up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
# 구조물 길 알려주기
structure = {1: [up, down, left, right], 2: [up, down], 3: [left, right], 4: [up, right], 5: [down, right], 6: [down, left], 7: [up, left]}

# 범인 잡으러 갈 함수 정의_BFS
def catch(x, y):
    # 칸 수 셀 변수
    cnt = 1
    # 가능성 넣을 변수. 디큐로.
    point = deque()
    point.append((x, y))
    # 다녀온 곳 확인
    tunnel_check[x][y] = 1
    while point:
        x, y = point.popleft()
        # l시간 지났으면 종료
        if tunnel_check[x][y] == l:
            return cnt
        # 다음 자리
        for dx, dy in structure[tunnel[x][y]]:
            nx = x + dx
            ny = y + dy
            # 구조물을 벗어나는지 확인
            if 0 > nx or nx >= n or 0 > ny or ny >= m:
                continue
            # 확인한 자리인지, 길이 없는지 확인
            if tunnel_check[nx][ny] != 0 or tunnel[nx][ny] == 0:
                continue
            # 구조물에 저장된 길
            for ddx, ddy in structure[tunnel[nx][ny]]:
                # 가고싶은 곳도 내쪽으로 열려있는지.
                if dx * ddx + dy * ddy == -1:
                    # 갈 수 있다면 가능성에 추가하고 다녀왔다고 체크
                    point.append((nx, ny))
                    tunnel_check[nx][ny] = tunnel_check[x][y] + 1
                    cnt += 1
                    # 확인했으니까 그만.
                    break
    return cnt

# 주어주는 입력 받기
T = int(input())
for tc in range(1, 1+T):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    tunnel_check = [[0] * m for _ in range(n)]
    # 시작점 넣어서 함수 시작
    ans = catch(r, c)
    print(f'#{tc}', ans)