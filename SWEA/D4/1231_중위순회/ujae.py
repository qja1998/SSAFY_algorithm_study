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
 
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value,end="")
        inorder_traversal(root.right)
 
for test_case in range(10):
    N = int(input())
    tree_dict = {}
    for _ in range(N):
        node_num, *node_info = input().split()
        tree_dict[node_num] = node_info
 
    root = make_tree(tree_dict,'1')
    print(f"#{test_case+1}",end=" ")
    inorder_traversal(root)
    print()