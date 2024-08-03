import sys
from collections import defaultdict
input = sys.stdin.readline

class FlowerNode:
    def __init__(self, xy: tuple, a=None, b=None, c=None, d=None):
        self.xy = xy
        self.a = a
        self.b = b
        self.c = c
        self.d = d

def set_dir(node1: FlowerNode, node2: FlowerNode, ad_bc: str):
    if ad_bc == 'ad':
        node1.a = node2
        node2.d = node1
        
    elif ad_bc == 'bc':
        node1.b = node2
        node2.c = node1

def remove_node(node: FlowerNode):
    nodeA, nodeD, nodeB, nodeC = node.a, node.d, node.b, node.c
    if nodeA != None:
        if nodeD != None:
            nodeA.d = nodeD
            nodeD.a = nodeA
        else:
            nodeA.d = None
    elif nodeD != None:
        nodeD.a = None
        
    if nodeB != None:
        if nodeC != None:
            nodeB.c = nodeC
            nodeC.b = nodeB
        else:
            nodeB.c = None
    elif nodeC != None:
        nodeC.b = None

n, k = map(int, input().split())
path = input().strip()
ad_list, bc_list = [], []

for i in range(n):
    x, y = map(int, input().split())
    ad_list.append([x - y, x])
    bc_list.append([x + y, x])
    if i == 0: start = (x, y)

ad_list.sort()
bc_list.sort()
node_dict = {}
for i in range(n):
    ad = ad_list[i]
    bc = bc_list[i]
    
    if i < n - 1:
        x = ad[1]
        y = x - ad[0]
        
        if (x, y) in node_dict:
            node = node_dict[(x, y)]
        else:
            node = FlowerNode((x, y))
            node_dict[(x, y)] = node
    
        next_ad = ad_list[i + 1]
        if ad[0] == next_ad[0]:
            next_x = next_ad[1]
            next_y = next_x - next_ad[0]
            if (next_x, next_y) in node_dict:
                next = node_dict[(next_x, next_y)]
            else:
                next = FlowerNode((next_x, next_y))
                node_dict[(next_x, next_y)] = next
            set_dir(node, next, 'ad')

        x = bc[1]
        y = bc[0] - x
        
        if (x, y) in node_dict:
            node = node_dict[(x, y)]
        else:
            node = FlowerNode((x, y))
            node_dict[(x, y)] = node
        
        next_bc = bc_list[i + 1]
        if bc[0] == next_bc[0]:
            next_x = next_bc[1]
            next_y = next_bc[0] - next_x
            if (next_x, next_y) in node_dict:
                next = node_dict[(next_x, next_y)]
            else:
                next = FlowerNode((next_x, next_y))
                node_dict[(next_x, next_y)] = next
            set_dir(node, next, 'bc')

node = node_dict[start]

for p in path:
    if p == 'A' and node.a != None:
        next = node.a
        remove_node(node)
        node = next
    elif p == 'B' and node.b != None:
        next = node.b
        remove_node(node)
        node = next
    elif p == 'C'and node.c != None:
        next = node.c
        remove_node(node)
        node = next
    elif p == 'D'and node.d != None:
        next = node.d
        remove_node(node)
        node = next

print(node.xy[0], node.xy[1])
