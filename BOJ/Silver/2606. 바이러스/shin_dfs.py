def dfs(start_idx=1):
    visited[start_idx] = 1
    for ni in arr[start_idx]:
        if visited[ni] == 0:
            dfs(ni)


com_num = int(input())
node_num = int(input())
arr = [[] for i in range(com_num + 1)]
visited = [0] * (com_num + 1)
for _ in range(node_num):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs()
print(sum(visited) - 1)