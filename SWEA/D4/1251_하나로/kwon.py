import heapq
from math import sqrt
from collections import defaultdict
TC = int(input())

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

for t in range(1, TC+1):
    N = int(input())

    land_x = list(map(int, input().split()))
    land_y = list(map(int, input().split()))

    lands = [[x, y] for x, y in zip(land_x, land_y)]

    E = float(input())

    # 가중치를 계산하여 그래프 만들기
    connect_dict = defaultdict(list)
    for i, land1 in enumerate(lands):
        for j, land2 in enumerate(lands[i+1:], start=i+1):
            cost = E * distance(*land1, *land2)**2
            connect_dict[i].append([j, cost])
            connect_dict[j].append([i, cost])

    first_land = list(connect_dict.keys())[0]

    min_heap = [[w, first_land, e] for e, w in connect_dict[first_land]]
    heapq.heapify(min_heap)

    visited = set([first_land])
    mst = []

    # MST 만들기 (PRIM)
    while min_heap:
        # 가중치가 작은 간선 선택
        w, s, e = heapq.heappop(min_heap)

        if e in visited:
            continue

        mst.append(w)
        visited.add(e)

        # 선택한 간선과 인접한 노드 힙에 추가
        for ne, nw in connect_dict[e]:
            if ne in visited:
                continue
            heapq.heappush(min_heap, [nw, e, ne])

    print(f"#{t} {int(round(sum(mst), 1))}")