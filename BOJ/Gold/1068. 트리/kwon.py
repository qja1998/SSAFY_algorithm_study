from collections import defaultdict
N = int(input())

tree = defaultdict(list)

start = 0
for node, parent in enumerate(list(map(int, input().split()))):
    if parent == -1:
        start = node
        continue
    tree[parent].append(node)

remove_node = int(input())

ans = 0

def dfs(node):
    global ans
    children = tree[node]
    if node == remove_node:
        return
    if len(children) == 0:
        ans += 1
        return
    elif len(children) == 1 and children[0] == remove_node:
        ans += 1
        return
    for child in children:
        dfs(child)

dfs(start)

print(ans)