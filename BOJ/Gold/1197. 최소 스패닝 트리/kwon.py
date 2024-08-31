import heapq
from collections import defaultdict

def prim(vertices, edges):
    mst = []

    adj_list = defaultdict(list)
    for s, e, w in edges:
        adj_list[s].append((e, w))
        adj_list[e].append((s, w))
    
    visited = set()
    # 초기 정점으로 초기화
    init_vertex = vertices[0]
    min_heap = [[w, init_vertex, e] for e, w in adj_list[init_vertex]]
    heapq.heapify(min_heap)
    visited.add(init_vertex)

    while min_heap:
        w, s, e = heapq.heappop(min_heap)
        if e in visited:
            continue

        visited.add(e)
        mst.append((s, e, w))

        for adj_v, adj_w in adj_list[e]:
            if adj_v in visited:
                continue
            heapq.heappush(min_heap, [adj_w, e, adj_v])
    return mst

def main():
    V, E = map(int, input().split())

    edges = []
    vertices = set()
    for _ in range(E):
        s, e, w = map(int, input().split())
        vertices.add(s)
        vertices.add(e)
        edges.append([s, e, w])
    vertices = list(vertices)

    answer = 0
    for _, _, w in prim(vertices, edges):
        answer += w
    
    print(answer)

if __name__ == '__main__':
    main()