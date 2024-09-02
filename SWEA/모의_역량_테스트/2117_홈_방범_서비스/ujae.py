def make_area(start_row, start_col, K):
    area = set()
    count = 0
    # 마름모 형태의 서비스 영역 좌표 계산
    for i in range(K):
        num = 2 * (K - 1) - (2 * i)
        for j in range(i + 1):
            area.add((start_row + i, start_col + j))
            area.add((start_row + i, start_col - j))
            area.add((start_row + i + num, start_col + j))
            area.add((start_row + i + num, start_col - j))
 
    # 서비스 영역 내 집의 수 세기
    for location in home_info:
        if location in area:
            count += 1
 
    # 운영 비용 계산
    operating_cost = K * K + (K - 1) * (K - 1)
 
    if count * M >= operating_cost:
        return count  # 수익이 운영 비용 이상인 경우 집의 수 반환
    return 0
 
def search_area(K):
    max_count = 0
    for i in range(-(K+1),N-(K+1)):
        for j in range(N):
            count = make_area(i, j, K)
            max_count = max(max_count, count)
    return max_count
 
 
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    home_location = [list(map(int, input().split())) for _ in range(N)]
 
    # 집의 위치 저장
    home_info = {(q, w) for q in range(N) for w in range(N) if home_location[q][w] == 1}
 
    max_homes = 0
    if len(home_info)*M >= (N+1)**2 + N**2:
        print(f"#{test_case} {len(home_info)}")
        continue
 
 
    # 가능한 K의 범위 (1부터 N)
    for K in range(1, N + 2):
        max_homes = max(max_homes, search_area(K))
 
    print(f"#{test_case} {max_homes}")