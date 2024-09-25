# 양방향 확인
H, W = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, W - 1
left_max, right_max = arr[left], arr[right]
result = 0

while left <= right:
    if left_max <= right_max:
        if arr[left] < left_max:
            result += left_max - arr[left]
        else:
            left_max = arr[left]
        left += 1
    else:
        if arr[right] < right_max:
            result += right_max - arr[right]
        else:
            right_max = arr[right]
        right -= 1

print(result)


# from collections import deque
#
# H, W = map(int, input().split())
# arr = list(map(int, input().split()))
# queue = deque(arr)
# start = end = check_num = p_num = 0
# check_box = []
# result = 0
#
# while queue:
#     p_num = start = queue.popleft()
#     end = 0
#     check_box = []
#     while True:
#         check_num = queue.popleft()
#         if check_num > p_num and check_num >= start:
#             end = check_num
#             break
#         check_box.append(check_num)
#         p_num = check_num
#     min_check = min(start, end)
#     result += sum(list(map(lambda x: min_check - x, check_box)))
#
# print(result)

# from collections import deque
#
# H, W = map(int, input().split())
# arr = list(map(int, input().split()))
# queue = deque(arr)
# start = end = check_num = p_num = 0
# check_box = []
# result = 0
#
# while queue:
#     p_num = start = queue.popleft()
#     end = 0
#     check_box = []
#
#     while queue:  # queue가 비어 있지 않은지 확인
#         check_num = queue.popleft()
#         if check_num > p_num and check_num >= start:
#             end = check_num
#             break
#         if not queue:
#             end = check_num
#             break
#         check_box.append(check_num)
#         p_num = check_num
#
#     min_check = min(start, end)
#     result += sum(list(map(lambda x: min_check - x, check_box)))
#
# print(result)


# from collections import deque
#
# H, W = map(int, input().split())
# arr = list(map(int, input().split()))
# queue = deque(arr)
# start = end = check_num = p_num = 0
# check_box = []
# result = 0
#
# while queue:
#     p_num = start = queue.popleft()
#     end = 0
#     check_box = []
#
#     while queue:  # queue가 비어 있지 않은지 확인
#         check_num = queue.popleft()
#
#         if check_num > p_num:  # 현재 수보다 큰 값이 나오면 끝점으로 설정
#             end = check_num
#             break
#
#         check_box.append(check_num)
#         p_num = check_num
#
#     # 끝점이 유효한 경우에만 빗물 계산
#     if end > start:
#         min_check = min(start, end)
#         result += sum(max(0, min_check - x) for x in check_box)
#
# print(result)

