from collections import deque

N, K = list(map(int, input().split()))

# X => X-1 or X+1 or X*2 로 이동

queue = deque([(N, 0)])
visited = [False] * 100001

def bfs():
    while queue:
        now = queue.popleft()
        if now[0]==K:
            return now[1]
        else:
            if now[0] >= 0 and now[0] <= 100000:
                if not visited[now[0]]:
                    queue.append((now[0]-1, now[1]+1))
                    queue.append((now[0]+1, now[1]+1))
                    queue.append((now[0]*2, now[1]+1))
                    visited[now[0]] = True

print(bfs())
