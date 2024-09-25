import sys
sys.stdin = open('sample_input.txt')

# dfs 사용
# depth는 현재 탐색 깊이, 석택한 수
# crt_cnt는 현재 채취한 꿀의 양
# crt_sum은 꿀의 양에 따른 수익
# x와 y는 해당 좌표
def harvest_honey(depth, crt_cnt, crt_sum, x, y):
    global max_val
    if crt_cnt > C:  # 꿀의 양이 최대 용량 초과시 탐색 종료
        return
    if depth == M:  # 선택한 수가 최대 수(M)에 도달 했을 때
        max_val = max(max_val, crt_sum)  # 현재 제곱의 합과 최대 제곱 합중 큰 것 업데이트
        return

    # 해당 꿀을 선택 했을 경우
    harvest_honey(depth + 1, crt_cnt + honey_grid[x][y + depth], crt_sum + honey_grid[x][y + depth] ** 2, x, y)
    # 해당 꿀을 선택하지 않고 다음 옆(depth)으로 넘길 경우
    harvest_honey(depth + 1, crt_cnt, crt_sum, x, y)


T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey_grid = [list(map(int, input().split())) for _ in range(N)]

    result, max_val = 0, 0
    memo = [[0] * N for _ in range(N)]  # 메모이제이션 초기화화

    # 모든 가능한 시작 위치에서 함수를 호출하여 각 위치에서의 최대 제곱 합을 계산
    for i in range(N):
        for j in range(N - M + 1):
            max_val = 0
            harvest_honey(0, 0, 0, i, j)
            memo[i][j] = max_val

    # 두 일꾼을 겹치지 않게 벌통을 선택하는 방법
    for x1 in range(N):
        # 가로로 연속되도록 M개의 벌통을 선택하고,
        # 선택한 벌통에서 꿀을 채취하기 때문에 해당 인덱스 전까지만 확인
        # N - M + 1
        for y1 in range(N - M + 1):
            # 바로 옆으로 두 번째 일꾼이 채취할 경우를 생각해서 x1에서 시작
            # 조건으로 같은 행일 때,
            # 첫 번째 벌통이 (0, 1)에서 시작하고 M이 2라면, 두 번째 벌통은 (0, 3)에서 시작
            # 두 벌통이 서로 겹치지 않도록 보장
            # 서로 다른 행이라면, 두 번째 일꾼의 열을 0부터 가능하도록 허용
            for x2 in range(x1, N):
                y2_start = y1 + M if x1 == x2 else 0
                for y2 in range(y2_start, N - M + 1):
                    # 두 일꾼이 채집한 벌통의 꿀 제곱 합을 더하여 result 갱신
                    result = max(result, memo[x1][y1] + memo[x2][y2])

    print(f"#{tc} {result}")
