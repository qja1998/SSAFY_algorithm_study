test_case = int(input())

def make_subset(nums, n, subset=[], subset_num=0):
    global result
    # 합이 목표에 도달한 경우
    if subset_num == k:
        result += 1
        return
    # nums를 모두 순회한 경우
    if n == 0:
        return

    # 현재 원소를 고르는 경우
    make_subset(nums[:n - 1], n - 1, subset + [nums[n - 1]], subset_num + nums[n - 1])
    # 현재 원소를 고르지 않는 경우
    make_subset(nums[:n - 1], n - 1, subset, subset_num)

for t in range(test_case):
    n, k = map(int, input().split())

    nums = list(map(int, input().split()))

    result = 0

    make_subset(nums, n)

    print(f"#{t + 1} {result}")