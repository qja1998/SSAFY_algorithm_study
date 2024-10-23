import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        next_node = graph[node] # 인덱스 번호에 해당하는 곳 방문

        if next_node in visited:
            if next_node == start: # 그 인덱스에 있는 값이 이미 방문했던 인덱스 번호와 같으면 다시 돌아왔다는 뜻 (순환)
                for v in visited: # 여기까지 방문한 노드들을 추가
                    result.add(v)
            return

        visited.add(next_node)
        queue.append(next_node)

N = int(input())
graph = [0] + [int(input()) for _ in range(N)] # 인덱스 1번부터 입력이 들어감
result = set()

for i in range(1, N + 1):
    if i not in result:
        bfs(i)

print(len(result))
for num in sorted(result):
    print(num)
