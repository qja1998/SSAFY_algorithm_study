# from collections import deque
#
# N = int(input())
# arr = list(map(int, input().split()))
# erase_N = int(input())
# arr_check = [[] for _ in range(N)]
#
# for i in range(N):
#     if arr[i] == -1:
#         continue
#     arr_check[arr[i]].append(i)
#
# queue = deque([erase_N])
# exclude_node = []
#
#
# def check_exclude_node():
#     global exclude_node
#
#     while queue:
#         e = queue.popleft()
#         for ac in arr_check[e]:
#             queue.append(ac)
#         exclude_node.append(e)
#     return
#
#
# check_exclude_node()
#
# result = 0
#
# for i in range(N):
#     if i not in exclude_node:
#         if not arr_check[i]:
#             result += 1
#
# print(result)

from collections import deque

N = int(input())
arr = list(map(int, input().split()))
erase_N = int(input())
arr_check = [[] for _ in range(N)]

root = -1

# 트리 구성: 각 노드의 자식 목록을 arr_check에 저장
for i in range(N):
    if arr[i] == -1:
        root = i  # 루트 노드 저장
    else:
        arr_check[arr[i]].append(i)

# 삭제할 노드가 루트인 경우, 트리가 사라지므로 리프 노드는 0개
if erase_N == root:
    print(0)
else:
    # 삭제된 노드를 포함한 모든 자식 노드를 제거
    queue = deque([erase_N])
    exclude_node = set()

    while queue:
        e = queue.popleft()
        exclude_node.add(e)
        for child in arr_check[e]:
            queue.append(child)

    # 남은 트리에서 리프 노드 개수 세기
    result = 0
    for i in range(N):
        if i not in exclude_node:  # 삭제된 노드가 아니고
            if not arr_check[i]:  # 자식이 없는 노드
                result += 1
            elif all(child in exclude_node for child in arr_check[i]):  # 모든 자식이 삭제된 경우
                result += 1

    print(result)
