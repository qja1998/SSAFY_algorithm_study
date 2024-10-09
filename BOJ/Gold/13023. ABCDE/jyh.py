from collections import defaultdict

def dfs(node, depth):
    if depth >= 4:
        return True

    visited.append(node)

    for this_n in graph[node]:
        if this_n not in visited:
            if dfs(this_n, depth + 1):
                return True

    # 회복
    visited.remove(node)
    return False

N, M = map(int, input().split())
graph = defaultdict(list)
for i in range(M):
    a, b = map(int, input().split())
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]
    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

visited = []

for i in range(N):
    if dfs(i, 0):  # 깊이 0에서 시작
        print(1)
        exit()

print(0)
