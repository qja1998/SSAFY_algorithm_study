from itertools import combinations

# (r, c) r: y값, c: x값

N, M = map(int, input().split())
city_info = [list(map(int, input().split())) for _ in range(N)]
chicken_info = []
house_info = []

for y in range(N):
    for x in range(N):
        if city_info[y][x] == 1:
            house_info.append((y, x))
        elif city_info[y][x] == 2:
            chicken_info.append((y, x))

min_chicken_distance = 9999

for chicken_comb in combinations(chicken_info, M):
    total_distance = 0
    for hy, hx in house_info:
        min_distance = min(abs(cy - hy) + abs(cx - hx) for cy, cx in chicken_comb)
        total_distance += min_distance
    min_chicken_distance = min(min_chicken_distance, total_distance)

print(min_chicken_distance)
