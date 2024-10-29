from itertools import combinations

INF = float('inf')
N, M = map(int, input().split())

house = []
chicken = []

def get_dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

for y in range(N):
    for x, num in enumerate(map(int, input().split())):
        if num == 1:
            house.append((x, y))
        elif num == 2:
            chicken.append((x, y))

min_total = INF
for comb in combinations(chicken, M):
    total = 0
    
    for h_pos in house:
        min_dist = INF
        for ch_pos in comb:
            min_dist = min(min_dist, get_dist(h_pos, ch_pos))
        total += min_dist
    
    min_total = min(min_total, total)

print(min_total)