from collections import deque


def bfs(start_idx=1):
    visited[start_idx] = 1
    queue = deque([1])
    while queue:
        crt_idx = queue.popleft()
        for ni in arr[crt_idx]:
            if visited[ni] == 0:
                queue.append(ni)
                visited[ni] = 1
    return


com_num = int(input())
node_num = int(input())
arr = [[] for i in range(com_num + 1)]
visited = [0] * (com_num + 1)
for _ in range(node_num):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

bfs()
print(sum(visited) - 1)