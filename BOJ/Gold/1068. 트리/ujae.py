from collections import defaultdict, deque

N = int(input())
node_info = list(map(int, input().split()))
delete_node = int(input())

tree_info = defaultdict(list)

for i in range(len(node_info)):
    tree_info[node_info[i]].append(i)

count = 0
have_to_del = [delete_node]
queue = deque([delete_node])
while queue:
    node = queue.popleft()
    if len(tree_info[node]) != 0:
        have_to_del.extend(tree_info[node])
        queue.extend(tree_info[node])

for key in tree_info:
    tree_info[key] = [value for value in tree_info[key] if value not in have_to_del]

for i in range(N):
    if i not in have_to_del:
        if len(tree_info[i]) == 0:
            count += 1

print(count)
