def count_leaf_nodes(n, parent, delete_node):
    # 트리 구조를 저장하기 위한 리스트
    tree = [[] for _ in range(n)]
    
    # 트리 구성 (각 노드의 자식들을 저장)
    root = -1
    for i in range(n):
        if parent[i] == -1:
            root = i
        else:
            tree[parent[i]].append(i)

    # 삭제할 노드와 그 자손들을 트리에서 제거하는 함수
    def delete_subtree(node):
        tree[node] = []  # 자식 노드 정보 삭제
        for i in range(n):
            if node in tree[i]:
                tree[i].remove(node)  # 부모 노드로부터 삭제

    delete_subtree(delete_node)  # 삭제할 노드 및 자손들 제거
    
    # 리프 노드를 세기 위한 DFS 함수
    def count_leaves(node):
        if not tree[node]:  # 자식이 없다면 리프 노드
            return 1
        leaf_count = 0
        for child in tree[node]:
            leaf_count += count_leaves(child)
        return leaf_count
    
    # 삭제 후 루트 노드가 삭제된 경우 처리
    if delete_node == root:
        return 0
    
    # 루트에서 시작하여 리프 노드 개수 세기
    return count_leaves(root)

# 입력 처리
n = int(input())  # 노드의 개수
parent = list(map(int, input().split()))  # 각 노드의 부모 정보
delete_node = int(input())  # 삭제할 노드

# 결과 출력
print(count_leaf_nodes(n, parent, delete_node))