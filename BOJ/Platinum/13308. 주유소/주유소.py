import sys, heapq

def dijkstra():
    inf = 98765432109876543210
    # d : 상태 공간 배열
    d = [[inf] * (max(arr) + 1) for _ in range(n + 1)]
    q = []
    d[1][arr[1]] = 0
    heapq.heappush(q, (0, arr[1], 1)) # 이진트리 기반 최소 힙
    while q:
        # now_dist : 현재 드는 총 비용
        # now_cost : 현재 정점에서 다른 정점으로 갈 때 드는 단위 비용
        # now : 현재 정점
        now_dist, now_cost, now = heapq.heappop(q)
        if now == n: # 도착
            return now_dist
        if d[now][now_cost] < now_dist: # 기존 거리보다 멀면 제외
            continue
        for (next, next_dist) in adj[now]:
            next_cost = min(arr[next], now_cost) # 해당 도시를 거칠 때의 거리
            if d[next][now_cost] > now_dist + now_cost * next_dist: # 저장했던 가리보다 짧으면 교체
                d[next][now_cost] = now_dist + now_cost * next_dist
                heapq.heappush(q, (now_dist + now_cost * next_dist, next_cost, next)) # 다음 거리 계산을 위해 삽입

# 입력부
n, m = map(int, sys.stdin.readline().split())
arr = [-1] + list(map(int, sys.stdin.readline().split()))
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
    
# 정답 출력
print(dijkstra())