import sys
from collections import deque
sys.stdin = open('sample_input.txt')

# 4방향 탐색
dir_crd = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 중복 방문이 허용되는 bfs
def restore_area():
    global visited
    # 시작점을 미리 queue에 넣음
    queue = deque([(0, 0)])
    # 해당 시작점을 미리 갱신
    visited[0][0] = area_lst[0][0]

    # 큐가 모두 없어질 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 4 방향 탐색
        for dx, dy in dir_crd:
            nx, ny = x + dx, y + dy
            # 범위 내에 있는지, 이동할 위치가 더 적은 비용인지 비교
            # 이동할 위치 누적 비용 > 현 위치의 누적 비용 + 다음 위치에 대한 비용
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] > visited[x][y] + area_lst[nx][ny]:
                # 다음 좌표 큐에 삽입
                queue.append((nx, ny))
                # 계속해서 해당 좌표의 위치가 적은 누적 비용으로 갱신
                visited[nx][ny] = visited[x][y] + area_lst[nx][ny]
    # 도착 지점 반환
    return visited[N-1][N-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area_lst = [list(map(int, input())) for _ in range(N)]
    visited = [[float('inf')]*N for _ in range(N)]  # 방문처리 및 누적 비용 갱신할 배열 초기화

    result = restore_area()
    print(f"#{tc} {result}")
