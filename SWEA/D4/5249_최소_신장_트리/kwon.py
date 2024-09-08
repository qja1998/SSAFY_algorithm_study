import heapq
from collections import defaultdict

test_case = int(input())

for t in range(1, test_case+1):
    V, E = map(int, input().split())

    visited = set()
    mst = []
    e_dict = defaultdict(list)

    for _ in range(E):
        s, e, w = map(int, input().split())
        e_dict[s].append((e, w))
        e_dict[e].append((s, w))
    
    first_v = list(e_dict.keys())[0]
    e_list = [(w, first_v, e) for e, w in e_dict[first_v]]

    heapq.heapify(e_list)
    visited.add(first_v)

    while e_list:
        w, s, e = heapq.heappop(e_list)

        if e in visited:
            continue

        visited.add(e)
        mst.append(w)

        for n_e, n_w in e_dict[e]:
            if n_e in visited:
                continue
            heapq.heappush(e_list, (n_w, e, n_e))

    print(f"#{t} {sum(mst)}")