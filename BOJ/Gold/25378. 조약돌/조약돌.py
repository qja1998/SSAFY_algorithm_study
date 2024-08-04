n = int(input())
nums = list(map(int, input().split()))

check = [[0] * n for _ in range(n)]
memo = [0] * (n + 1)
memo[1] = 1

for l in range(n - 1):
    tmp = nums[l]

    for r in range(l + 1, n):
        if tmp == nums[r]:
            check[l][r] = 1
        elif tmp > nums[r]:
            break
        tmp = abs(tmp - nums[r])

for i in range(2, n + 1):
    new_min = float('inf')
    for j in range(1, i):
        if check[j - 1][i - 1] == 1:
            new = memo[j - 1] + i - j
            if new_min > new:
                new_min = new
            
    memo[i] = min(memo[i - 1] + 1, new_min)
print(memo[-1])
