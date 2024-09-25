from collections import deque

computer = int(input())
connect = int(input())
graph = {}
for i in range(connect):
    x, y = map(int, input().split())
    # 그래프로 만들기.
    if x not in graph:
        graph[x] = []
    graph[x].append(y)
    if y not in graph:
        graph[y] = []
    graph[y].append(x)
# print(graph)
# 1이 갈 수 있는 곳
q = deque([1])
# 다녀온 곳을 저장
visited = [1]

# dd가 아니면 key만 들어갔을 때 찾을 수 있는게 없음.
# graph가 부를 수 있는 값이 없어서 오류.

if not graph:
    print(0)
else:
# 그래프가 비었을 때를 따로 처리해 주면 돌아간다.
    cnt = 0
    while q:
        c_com = q.popleft()
        for n_com in graph[c_com]:
            # 이미 다녀온 곳이라면 지나가기
            if n_com in visited:
                continue
            # 아니라면 방문처리하고 큐에 더하기
            visited.append(n_com)
            q.append(n_com)
            # 카운트 올리기
            cnt += 1

    print(cnt)