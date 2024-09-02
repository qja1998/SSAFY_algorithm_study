class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
 
def make_tree(tree_dict, node_num):
    node_info_list = tree_dict[node_num]
    if len(node_info_list) == 1:
        node = TreeNode(node_info_list[0])
    elif len(node_info_list) == 2:
        node_value, left_key = node_info_list
        node = TreeNode(node_value)
        node.left = make_tree(tree_dict, left_key)
    else:
        node_value, left_key, right_key = node_info_list
        node = TreeNode(node_value)
        node.left = make_tree(tree_dict, left_key)
        node.right = make_tree(tree_dict, right_key)
    return node
 
def cal(root):
    if root.value.isdecimal():
        return root.value
    else:
        if root.value == "+":
            return int(cal(root.left)) + int(cal(root.right))
        elif root.value == "-":
            return int(cal(root.left)) - int(cal(root.right))
        elif root.value == "/":
            return int(cal(root.left)) / int(cal(root.right))
        else:
            return int(cal(root.left)) * int(cal(root.right))
         
for test_case in range(10):
    N = int(input())
    tree_dict = {}
    for _ in range(N):
        node_num, *node_info = input().split()
        tree_dict[node_num] = node_info
 
    root = make_tree(tree_dict,'1')
    result = int(cal(root))
 
    print(f'#{test_case+1} {result}')
