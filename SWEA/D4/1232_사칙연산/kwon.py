class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def make_tree(node_dict, node_num):
    node_info = node_dict[node_num]
    if len(node_info) == 1:
        node = Node(node_info[0])


    else:
        node_val, left, right = node_info
        node = Node(node_val)
        node.left = make_tree(node_dict, left)
        node.right = make_tree(node_dict, right)

    return node


def search(node):
    if node.data.isdigit():
        return int(node.data)
    else:
        operator = node.data
        if operator == '+':
            return search(node.left) + search(node.right)
        elif operator == '-':
            return search(node.left) - search(node.right)
        elif operator == '*':
            return search(node.left) * search(node.right)
        elif operator == '/':
            return search(node.left) / search(node.right)

for i in range(10):
    n = int(input())
    result = 0
    node_dict = dict()
    for _ in range(n):
        node_num, *node_info = input().split()
        # print(node_num, node_info)
        node_dict[node_num] = node_info

    root = make_tree(node_dict, '1')

    result = int(search(root))
    print(f"#{i+1} {result}")