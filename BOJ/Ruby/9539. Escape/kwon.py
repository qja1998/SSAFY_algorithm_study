import sys
# from collections import defaultdict
from heapq import heappop, heappush
sys.setrecursionlimit(50_000)

# 33_554_432
INF = float('inf')

def dfs(node, parent, values, adj):
    main = []

    # 자식 노드에 대해 DFS 실행
    for neighbor in adj[node]:
        if neighbor != parent:
            sub_healths = dfs(neighbor, node, values, adj)

            # 병합하기 전에 큰 애를 main으로 -> 병합시 for문 줄일 수 있음
            if len(main) < len(sub_healths):
                main, sub_healths = sub_healths, main

            # 작은 애를 큰 애한테 병합
            for health in sub_healths:
                heappush(main, health)

    # 현재 노드의 값 처리
    value = values[node]
    if value > 0:
        heappush(main, (0, value))  # 이익이 있는 경우 힙에 추가
    else:
        required = -value
        gain = value

        # 힙에서 회복을 사용하며 이익을 계산(작은 회복량부터 사용)
        # 회복을 할 수 있거나, 필요로 하는 체력보다 남은 체력이 많은 경우 중지
        while main and (gain <= 0 or required >= main[0][0]):
            health = heappop(main)
            required = max(required, -gain + health[0])
            gain += health[1]

        # 얻은 이익이 양수일 때만 힙에 추가
        if gain > 0:
            heappush(main, (required, gain))

    return main

def solve():
    input = sys.stdin.readline
    index = 0

    z = int(input())
    index += 1

    results = []
    for _ in range(z):
        n, destination = map(int, input().split())

        adj = [[] for _ in range(n + 1)]

        # 노드 값 입력
        values = [0] + list(map(int, input().split()))

        values[0] = INF  # 루트 노드 값

        # 인접 리스트
        adj[0].append(destination)
        adj[destination].append(0)

        for _ in range(n - 1):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)

        # DFS 실행 후 자산 계산
        final_assets = dfs(1, None, values, adj)
        have = 0
        
        # 마지막 회복
        while final_assets and final_assets[0][0] <= have:
            asset = heappop(final_assets)
            have += asset[1]

        # 결과 확인
        if have >= INF:
            results.append("escaped")
        else:
            results.append("trapped")

    print("\n".join(results))

if __name__ == "__main__":
    solve()
