from collections import deque

test_case = int(input())

for t in range(test_case):
    n, k = map(int, input().split())

    rotate_cnt = n // 4

    pw = deque(list(input()))

    result_nums = set()
    # 회전수
    for i in range(rotate_cnt):
        for j in range(0, n, rotate_cnt):
            result_num = int(''.join(list(pw)[j: j + rotate_cnt]), 16)
            result_nums.add(result_num)

        deque.rotate(pw, 1)

    result_nums = list(result_nums)
    result_nums.sort(reverse=True)

    print(f"#{t + 1} {result_nums[k - 1]}")
