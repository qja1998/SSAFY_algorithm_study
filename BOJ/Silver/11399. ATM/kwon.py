N = int(input())

nums = list(map(int, input().split()))

ans = 0
sum_num = 0

for num in sorted(nums):
    sum_num += num
    ans += sum_num

print(ans)