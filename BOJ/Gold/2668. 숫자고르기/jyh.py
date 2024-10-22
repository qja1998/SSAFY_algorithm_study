def dfs(v, visited, cycle, graph, start):
    visited[v] = True  # 현재 노드를 방문 처리
    next_node = graph[v]  # 다음 방문할 노드

    # 다음 노드를 방문하지 않았으면 계속 DFS 탐색
    if not visited[next_node]:
        if dfs(next_node, visited, cycle, graph, start):
            cycle.append(v)
            return True
    # 사이클이 발견된 경우 (시작점으로 다시 돌아온 경우)
    elif next_node == start:
        cycle.append(v)
        return True
    
    return False

def find_maximum_set(N, second_row):
    # 첫째 줄에서 두번째 줄로 연결되는 그래프 구성
    graph = [0] * (N + 1)
    for i in range(1, N + 1):
        graph[i] = second_row[i - 1]  # 첫째 줄 i에서 두번째 줄의 값 연결

    # 사이클을 찾기 위한 방문 배열
    visited = [False] * (N + 1)
    result = []  # 최종적으로 선택된 사이클을 저장할 리스트

    # 모든 노드에 대해 DFS 수행
    for i in range(1, N + 1):
        if not visited[i]:  # 방문하지 않은 경우에만 탐색
            cycle = []  # 사이클을 임시 저장할 리스트
            if dfs(i, visited, cycle, graph, i):
                result.extend(cycle)  # 사이클이 발견되면 결과에 추가

    return sorted(result)  # 오름차순으로 정렬하여 반환

# 입력 받기
N = int(input())  # N 입력 (첫째 줄의 칸 개수)
second_row = [int(input()) for _ in range(N)]  # 두번째 줄 값들 입력

# 결과 찾기
result = find_maximum_set(N, second_row)

# 출력
print(len(result))  # 뽑힌 정수들의 개수 출력
for num in result:
    print(num)  # 뽑힌 정수들을 작은 수부터 큰 수의 순서로 출력
