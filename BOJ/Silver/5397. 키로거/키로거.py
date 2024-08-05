import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())

class Node:
    def __init__(self, char, right=None, left=None) -> None:
        self.char = char
        self.right = right
        self.left = left

def command(node: Node, com: str) -> Node:
    if com.isalpha() or com.isdigit():
        new_node = Node(com, node.right, node)
        if node.right != None:
            node.right.left = new_node
        node.right = new_node
        node = node.right
    elif com == '<':
        if node.left != None:
            node = node.left
    elif com == '>':
        if node.right != None:
            node = node.right
    elif com == '-':
        if node.left != None:
            node.left.right = node.right
            if node.right != None:
                node.right.left = node.left
            node = node.left
    return node

for _ in range(n):
    string = input().strip()
    head = Node('*')
    node = head
    for c in string:
        node = command(node, c)
    node = head.right
    while node:
        print(node.char)
        node = node.right
    print('\n')