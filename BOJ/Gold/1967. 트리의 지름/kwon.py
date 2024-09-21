import sys
input = sys.stdin.readline

from collections import defaultdict, deque

n = int(input())

tree = defaultdict(dict)
for _ in range(n-1):
    p, c, w = map(int, input().split())
    tree[p][c] = w

def bfs(start):
    q = deque([[start, 0, 0]])
    visited = defaultdict(bool)
    fst_w = 0
    scd_w = 0
    while q:
        node, w, total_w = q.popleft()
        if w > 0:
            q.append([node, w-1, total_w])
            continue
        if not tree[node]:
            if total_w > fst_w:
                scd_w = fst_w
                fst_w = total_w
            elif total_w > scd_w:
                scd_w = total_w
            continue
        for child in tree[node]:
            c_w = tree[node][child]
            if visited[child]:
                continue
            q.append([child, c_w, w+c_w])
        
    return fst_w, scd_w

fst_w, scd_w = bfs(1)
print(fst_w - scd_w)