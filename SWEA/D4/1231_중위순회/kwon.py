TEST_CASE = 10


def tree_search(node_num, value, left=None, right=None):
    result = ''

    # 자식 노드가 있다면
    # if len(tree_dict[node_num]) == 3:
    if left:
        # 왼쪽 노드
        result += tree_search(node_num * 2, *tree_dict[node_num * 2])

        # 현재 노드
        result += value[0]

        if right:
            # 오른쪽 노드
            result += tree_search(node_num * 2 + 1, *tree_dict[node_num * 2 + 1])

    # 자식 노드가 없다면
    else:
        result += value[0]

    return result


for t in range(TEST_CASE):
    n = int(input())

    tree_dict = {i: input().split()[1:] for i in range(1, n + 1)}

    result = tree_search(1, *tree_dict[1])
    print(f"#{t + 1} {result}")
