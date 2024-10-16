def dfs_iterative(x, y, color):
    stack = [(x, y, -1, -1)]  # (현재 x, 현재 y, 이전 x, 이전 y)를 스택에 저장
    visited[x][y] = True  # 시작 위치 방문 처리

    while stack:
        x, y, px, py = stack.pop()

        # 상하좌우 네 방향으로 이동하며 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # 게임판 내부에 있고 이전 위치가 아니며 색상이 동일한 경우 탐색
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) != (px, py) and board[nx][ny] == color:
                # 이미 방문한 노드면 사이클이 발생한 것
                if visited[nx][ny]:
                    return True
                # 아직 방문하지 않았다면 스택에 넣고 방문 처리
                stack.append((nx, ny, x, y))
                visited[nx][ny] = True

    # 탐색이 끝날 때까지 사이클이 없으면 False 반환
    return False

# 입력 처리
N, M = map(int, input().split())  # N: 행, M: 열
board = [list(input().strip()) for _ in range(N)]  # 게임판 상태 입력
visited = [[False] * M for _ in range(N)]  # 방문 여부 저장하는 2차원 리스트

# 모든 좌표에 대해 DFS 탐색을 수행
for i in range(N):
    for j in range(M):
        # 아직 방문하지 않은 좌표에 대해 DFS 탐색
        if not visited[i][j]:
            # 스택 기반 DFS를 통해 사이클이 있는지 확인
            if dfs_iterative(i, j, board[i][j]):
                print("Yes")
                exit()  # 사이클이 발견되면 "Yes" 출력 후 프로그램 종료

# 모든 좌표를 탐색했지만 사이클이 없으면 "No" 출력
print("No")