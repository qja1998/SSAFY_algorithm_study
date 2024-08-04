k = int(input())

class Node:
    def __init__(self, n: int, left=None, right=None) -> None:
        self.n = n
        self.left = left
        self.right = right

head = Node(-1)
node = head

for i in range(k):
    next_node = Node(i + 1, node)
    node.right = next_node
    node = next_node

def remove_node(step: int) -> None:
    node = head
    while node:
        for _ in range(step):
            node = node.right
            if node == None:
                return
        if not node.left:
            return
        node.left.right = node.right
        if node.right:
            node.right.left = node.left
    

m = int(input())

for _ in range(m):
    r = int(input())
    remove_node(r)

node = head.right

while node:
    print(node.n)
    node = node.right