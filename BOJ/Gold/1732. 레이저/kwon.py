from collections import defaultdict
from math import atan2

N = int(input())

result = set()

# 기울기: 높이
laser_dict = defaultdict(list)
for _ in range(N):
    x, y, z = map(int, input().split())
    if x == 0 and y == 0:
        continue
    
    laser_dict[atan2(y, x)].append((x, y, z))

for a in laser_dict:
    laser_at_a = sorted(laser_dict[a], key=lambda x:abs(x[0]))
    
    max_h = -1
    for x, y, z in laser_at_a:
        # 앞보다 높음
        if max_h < z:
            max_h = z
        else: # 앞보다 낮거나 같음
            result.add((x, y))

for x, y in sorted(list(result)):
    print(x, y)