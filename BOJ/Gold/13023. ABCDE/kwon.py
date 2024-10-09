from collections import defaultdict, deque

freinds = defaultdict(list)

N, M = map(int, input().split())

for _ in range(M):
    a, b = map(int, input().split())
    freinds[a].append(b)
    freinds[b].append(a)

visited = []
ans = 0
