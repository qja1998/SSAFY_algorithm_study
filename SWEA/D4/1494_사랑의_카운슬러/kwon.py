import sys
from itertools import combinations
sys.stdin = open(r"C:\Users\SSAFY\Downloads\input (1).txt", "r") 

TC = int(input())

INF = float('inf')

for t in range(1, TC+1):
    n = int(input())

    positions = [tuple(map(int, input().split())) for _ in range(n)]

    positions.sort(key=lambda x: x[0]**2 + x[1]**2)

    selected_pos = combinations(positions, n//2)

    min_vec = INF
    for pos_list in selected_pos:
        pos_list2 = list(set(positions)-set(pos_list))

        sum_x, sum_y = 0, 0

        for (x1, y1), (x2, y2) in zip(pos_list, pos_list2):
            sum_x += x1 - x2
            sum_y += y1 - y2

        min_vec = min(min_vec, sum_x**2 + sum_y**2)

    
    print(f"#{t} {min_vec}")
        