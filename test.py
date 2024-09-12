import sys
from collections import defaultdict
from heapq import heappop, heappush

# 33_554_432
INF = float('inf')

def dfs(node, parent, values, adj):
    main = []

    # 자식 노드에 대해 DFS 실행
    for neighbor in adj[node]:
        if neighbor != parent:
            sub_assets = dfs(neighbor, node, values, adj)

            # 자산 병합: 더 큰 자원 집합을 main으로 설정
            if len(main) < len(sub_assets):
                main, sub_assets = sub_assets, main

            # 작은 자원 집합을 큰 집합에 병합
            for asset in sub_assets:
                heappush(main, asset)

    # 현재 노드의 값 처리
    value = values[node]
    if value > 0:
        heappush(main, (0, value))  # 이익이 있는 경우 힙에 추가
    else:
        required = -value
        gain = value

        # 힙에서 자원을 사용하며 이익을 계산
        while main and (gain <= 0 or required >= main[0][0]):
            asset = heappop(main)
            required = max(required, -gain + asset[0])
            gain += asset[1]

        # 얻은 이익이 양수일 때만 힙에 추가
        if gain > 0:
            heappush(main, (required, gain))

    return main

def solve():
    input = sys.stdin.read
    data = input().split()
    index = 0

    z = int(data[index])
    index += 1

    results = []
    for _ in range(z):
        n = int(data[index])
        index += 1

        values = [0] * (n + 1)  # 노드 값 저장
        adj = defaultdict(list)  # 인접 리스트

        destination = int(data[index])
        index += 1

        # 노드 값 입력
        for i in range(1, n + 1):
            values[i] = int(data[index])
            index += 1

        values[0] = INF  # 루트 노드 값

        # 인접 리스트 구축
        adj[0].append(destination)
        adj[destination].append(0)

        for _ in range(n - 1):
            a = int(data[index])
            b = int(data[index + 1])
            index += 2
            adj[a].append(b)
            adj[b].append(a)

        # DFS 실행 후 자산 계산
        final_assets = dfs(1, None, values, adj)
        have = 0
        
        # 힙에서 필요한 자원 사용
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
