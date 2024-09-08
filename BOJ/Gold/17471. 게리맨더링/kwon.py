from collections import defaultdict, deque

# 남은 노드가 모두 연결되면 True
def chk_connect(graph, selected):
    remain = total_set - set(selected)
    node_cnt = 0
    
    q = deque()
    while q:
        c_node = q.popleft()
        node_cnt += 1
        for n_node in graph[c_node]:
            if n_node in selected:
                continue
            q.append(n_node)

    return len(remain) == node_cnt

def gerrymandering(graph, node, neighbors, selected=[]):
    for i, neighbor in enumerate(neighbors):
        # 해당 노드를 선택하는 경우
        gerrymandering(graph, node, neighbors[i+1:], selected+[neighbor])
        # 해당 노드를 선택하지 않는 경우
        gerrymandering(graph, node, neighbors[i+1:], selected)

N = int(input())

people = list(map(int, input().split()))

graph = defaultdict(list)

total_set = set(range(1, N+1))

for i in range(1, N+1):
    neighbor = list(map(int, input().split()))[1:]
    for n in neighbor:
        graph[i].append(n)
        graph[n].append(i)

min_diff = float('inf')