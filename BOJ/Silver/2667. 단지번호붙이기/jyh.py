# 입력
N = int(input())
map_data = [list(map(int, input())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 여부 리스트
visited = [[False] * N for _ in range(N)]
# 각 단지 내 집의 수
complexes = []

def dfs(x, y):
    # 현재 위치 방문 처리
    count = 1
    visited[x][y] = True
    # 상하좌우로 이동하면서 연결된 집을 찾음
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 좌표가 지도 안에 있는지, 방문여부, 집이 있는지 확인
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and map_data[nx][ny] == 1:
            # 재귀
            count += dfs(nx, ny)
    return count  # 연결된 집의 개수를 반환

# 지도 전체를 탐색하며 단지를 찾음
for i in range(N):
    for j in range(N):
        # 현재 위치에 집이 있고, 아직 방문하지 않은 경우 찾기
        if map_data[i][j] == 1 and not visited[i][j]:
            # 함수실행
            complex_size = dfs(i, j)
            complexes.append(complex_size)  # 집 수 리스트에 추가

complexes.sort()  # 단지 내 집 오름차순 정렬
print(len(complexes))  # 총 단지수를 출력
for size in complexes:
    print(size)  # 각 단지에 속하는 집의 수를 출력
