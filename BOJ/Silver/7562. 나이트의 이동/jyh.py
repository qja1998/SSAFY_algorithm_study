import sys
sys.stdin = open('7562.txt', 'r')


from collections import deque

# 나이트가 이동할 수 있는 8가지 방향 정의
dx = [2, 2, 1, 1, -1, -1, -2, -2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(l, start, end):
    # 체스판 방문 여부 기록
    visited = [[False] * l for _ in range(l)]
    # BFS 탐색을 위한 큐 (현재 위치와 이동 횟수를 저장)
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True

    while queue:
        x, y, moves = queue.popleft()

        # 목표 위치에 도달하면 이동 횟수를 반환
        if (x, y) == (end[0], end[1]):
            return moves

        # 나이트가 이동할 수 있는 8방향 탐색
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            # 체스판 내에서 이동 가능한 경우만 큐에 추가
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves + 1))

    return -1  # 도달할 수 없는 경우

# 입력받기
T = int(input())
for tc in range(T):
    l = int(input())  # 체스판의 크기
    start = tuple(map(int, input().split()))  # 나이트의 현재 위치
    end = tuple(map(int, input().split()))  # 나이트가 이동하려는 목표 위치

    # 결과 출력 (최소 이동 횟수)
    print(bfs(l, start, end))