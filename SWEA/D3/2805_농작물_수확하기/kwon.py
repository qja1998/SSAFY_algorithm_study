test_case = int(input())

for t in range(test_case):
    n = int(input())
    nums = [[int(num) for num in input()] for _ in range(n)]

    result = sum(nums[n // 2])

    mid = n // 2

    for i in range(mid):
        row1 = nums[i]
        row2 = nums[n - i - 1]
        result += sum(row1[mid - i:mid + i + 1]) + sum(row2[mid - i:mid + i + 1])

    print(f'#{t+1} {result}')