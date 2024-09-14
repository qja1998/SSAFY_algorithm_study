from collections import defaultdict, deque

N = int(input())
M = int(input())

graph = defaultdict(list)
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

q = deque([1])
visited = [1]

cnt = 0
while q:
    c_com = q.popleft()

    for n_com in graph[c_com]:
        if n_com in visited:
            continue
        visited.append(n_com)
        q.append(n_com)
        cnt += 1

print(cnt)