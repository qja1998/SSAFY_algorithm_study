import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

def bfs(N):
    queue = deque([N])
    visited[N] = True

    while queue:
        c_loc = queue.popleft()

        if c_loc == K:
            return visited[c_loc]

        n_loc = [c_loc + 1, c_loc - 1, c_loc * 2]
        for next in n_loc:
            if 0 <= next <= MAX and visited[next] == False:
                visited[next] = visited[c_loc] + 1 # 걸린 시간을 다음 위치에 누적해주기
                queue.append(next)

N, K = map(int, input().split())
MAX = 100000

visited = [False] * (MAX + 1)
print(bfs(N) - 1)