# 1. 미세먼지 확산
# - (r, c) -> 인접한 4방향 확산
# - 인접한 방향에 공기청정기 or 벽 -> 확산x
# - 확산량: A(r, c)/5 (소수점 버림)
# - (r, c)에 남은 미세먼지 양 = A(r, c) - A(r, c)/5(소수점 버림) * 확산된 방향 수

# 2. 공기청정기 작동
# - 공기 청정기에서 바람 나옴
# - 위쪽 공기청정기 바람은 반시계 방향 순환, 아래쪽 공기청정기 바람은 시계방향 순환
# - 바람 불면 미세먼지가 바람 방향대로 한 칸씩 이동
# - 공기청정기로 바람 들어가면 미세먼지 정화됨


dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 시계방향


def main():
    R, C, T = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(R)]

    while T:
        # 1. 미세먼지 있는 지점 구하기
        dust_loc = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] > 0:
                    dust_loc.append((i, j))

        # 2. 확산시키기
        # 2-1. 확산 위치 구하기
        diffusion = []
        for x, y in dust_loc:
            diff_dust = 0
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                if grid[i][j] == -1:
                    continue

                dust = grid[x][y]//5
                diffusion.append((nx, ny, dust))
                diff_dust += dust
            diffusion.append((x, y, grid[x][y] - diff_dust))

        # 2-2. 확산시키기
        for x, y, dust in diffusion:
            grid[x][y] = dust

        # 3. 공기청정하기

if __name__ == "__main__":
    main()