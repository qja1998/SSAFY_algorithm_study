from collections import defaultdict
TC = int(input())

INF = float('inf')

def floyd(graph, start):
    v_len = len(graph)

    dist = [[INF] * v_len for _ in range(v_len)]

    for i in range(v_len):
        dist[i][i] = 0

    # 그래프의 가중치로 거리 행렬을 초기화
    for u in range(v_len):
        for v in range(v_len):
            if graph[u][v] != 0:
                dist[u][v] = graph[u][v]

    for k in range(v_len): # 모든 정점을 경유 정점으로 고려
        for i in range(v_len):
            for j in range(v_len):
                # 경유 정점 k를 통애 가는 경로가 더 짧은 경우 거리 행렬을 업데이트
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

for t in range(1, TC+1):
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            
            if matrix[i][j] == 0:
                matrix[i][j] = INF
    
    distances = floyd(matrix, 0)
    print(f"#{t} {max(map(max, distances))}")