def dfs(visit, start):
    visited[visit] = 1
    # print(visited)

    for crt in graph[visit]:
        # print('crt : ', crt)
        if not visited[crt]:
            dfs(crt, start)
        elif visited[crt] and crt == start:
            result.append(crt)
            # print('result : ', result)


N = int(input())

graph = [[] for _ in range(N + 1)]
result = []

for i in range(1, N + 1):
    graph[int(input())].append(i)

for i in range(1, N + 1):
    visited = [0] * (N + 1)
    dfs(i, i)

print(len(result))
for j in result:
    print(j)
