from collections import defaultdict, deque
from itertools import combinations

INF = float('inf')

def gerrymandering(graph, selected):
    q = deque([selected[0]])
    visited = [selected[0]]
    _sum_p = 0
    while q:
        node = q.popleft()
        _sum_p += people[node]

        for neighbor in graph[node]:
            if neighbor not in selected:
                continue
            if neighbor in visited:
                continue
            q.append(neighbor)
            visited.append(neighbor)

    # 골라진 선거구를 모두 돌지 못함
    if len(selected) != len(visited):
        return -1
    return _sum_p


N = int(input())

people = [0] + list(map(int, input().split()))

graph = defaultdict(list)

total_set = set(range(1, N+1))

for i in range(1, N+1):
    neighbor = list(map(int, input().split()))[1:]
    for n in neighbor:
        graph[i].append(n)
        graph[n].append(i)

min_diff = INF

for i in range(1, N//2+1):
    for comb1 in combinations(total_set, i):
        comb2 = tuple(total_set - set(comb1))
        sum_p1 = gerrymandering(graph, comb1)
        if sum_p1 == -1:
            continue
        sum_p2 = gerrymandering(graph, comb2)
        if sum_p2 == -1:
            continue
        min_diff = min(min_diff, abs(sum_p1 - sum_p2))

if min_diff == INF:
    print(-1)
else:
    print(min_diff)