N, M = map(int, input().split())
graph = [[0] * (M + 1) for _ in range(N + 1)]
result = 0

def dfs(depth):
    global result
    if depth == N * M:
        result += 1
        return
    x = depth // M + 1
    y = depth % M + 1

    if graph[x - 1][y] == 0 or graph[x - 1][y - 1] == 0 or graph[x][y - 1] == 0:
        graph[x][y] = 1
        dfs(depth+1)
        graph[x][y] = 0
    dfs(depth+1)

dfs(0)
print(result)
