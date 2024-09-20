from collections import defaultdict
H, W = map(int, input().split())

wall_dict = defaultdict(list)
max_wall = 0
for i, wall in enumerate(map(int, input().split())):
    for h in range(1, wall+1):
        wall_dict[h].append(i)
    max_wall = max(max_wall, wall)

water = 0
for h in range(max_wall, 0, -1):
    h_wall_list = wall_dict[h]
    if len(h_wall_list) == 1:
        continue
    water += max(h_wall_list) - min(h_wall_list) - len(h_wall_list) + 1

print(water)