N, M, B = map(int, input().split())
mapli = [list(map(int, input().split())) for _ in range(N)]

mapmax = max(map(max, mapli))
mapmin = min(map(min, mapli))

# 정답 구하기
min_time = float('inf')
best_height = 0

for this_h in range(mapmin, mapmax + 1):
    # 각 자리에서 min까지
    tomin = 0
    # 각 자리에서 max까지
    tomax = 0

    # 목표 높이와 비교하여 계산
    for i in range(N):
        for j in range(M):
            if mapli[i][j] > this_h:
                tomin += mapli[i][j] - this_h
            else:
                tomax += this_h - mapli[i][j]

    # 채울 블록을 가지고 있는지 확인
    if tomin + B >= tomax:
        time = tomin * 2 + tomax
        # 최소시간 갱신
        if time < min_time:
            min_time = time
            best_height = this_h
        if time == min_time:
            best_height = max(best_height, this_h)

# 결과 출력
print(min_time, best_height)