minus_num = list(range(1, 6))

for _ in range(10):
    t = int(input())

    nums = list(map(int, input().split()))

    min_num = min(nums) // 15 - 1
    nums = [num - (min_num * 15) for num in nums]

    minus_i = 0
    i = 0
    cur_num = nums[0]

    while True:
        i %= 8
        minus_i %= 5
        nums[i] -= minus_num[minus_i]
        cur_num = nums[i]
        if cur_num <= 0:
            break
        i += 1
        minus_i += 1

    nums[i] = 0
    nums = nums[i + 1:] + nums[:i + 1]
    nums = [str(num) for num in nums]
    print(f"#{t} {' '.join(nums)}")