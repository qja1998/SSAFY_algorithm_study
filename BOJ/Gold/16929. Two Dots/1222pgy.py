import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(si, sj, color):
    queue = deque()
    queue.append((si, sj, -1, -1))
    visited[si][sj] = True

    while queue:
        ci, cj, pi, pj = queue.popleft() # 현재 위치, 이전 위치
        for dx, dy in dxy:
            ni, nj = ci + dx, cj + dy
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] == color:
                    if not visited[ni][nj]:
                        queue.append((ni, nj, ci, cj))
                        visited[ni][nj] = True
                    # 이미 방문했지만 이전 위치와 다르면 처음으로 돌아왔다는 뜻이므로 사이클
                    elif (ni, nj) != (pi, pj):
                        return True
    return False

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if bfs(i, j, arr[i][j]):
                print("Yes")
                exit()  # 사이클을 찾으면 바로 종료

print("No")