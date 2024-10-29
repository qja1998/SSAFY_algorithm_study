from itertools import combinations

# 입력 받기
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken = []

# 집과 치킨집 각각 저장
for r in range(N):
    for c in range(N):
        if city[r][c] == 1:  # 해당 칸이 집(1)인 경우
            houses.append((r, c))  # houses 리스트에 (r, c) 좌표 추가
        elif city[r][c] == 2:  # 해당 칸이 치킨집(2)인 경우
            chicken.append((r, c))  # chicken_shops 리스트에 (r, c) 좌표 추가

min_cc_distance = 999999

# 치킨집 중 M개를 선택하는 모든 조합에 대해 최소 도시 치킨 거리 계산
for chicken_comb in combinations(chicken, M):  # 모든 치킨집 중 M개를 선택하는 조합 생성
    total_distance = 0  # 현재 선택된 치킨집 조합에 대한 총 도시 치킨 거리를 계산할 변수 초기화

    # 각 집에 대해 가장 가까운 치킨집과의 거리를 구하기
    for hr, hc in houses:
        min_distance = 9999
        for cr, cc in chicken_comb:
            # 거리계산
            distance = abs(hr - cr) + abs(hc - cc)
            # 최소값 갱신
            if distance < min_distance:
                min_distance = distance
        total_distance += min_distance

    # 현재 선택된 치킨집 조합에 대한 도시 치킨 거리가 최소값인지 확인
    if total_distance < min_cc_distance:
        min_cc_distance = total_distance  # 최소값 갱신

# 결과 출력
print(min_cc_distance)