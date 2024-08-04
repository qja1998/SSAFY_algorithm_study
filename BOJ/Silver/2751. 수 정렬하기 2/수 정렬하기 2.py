import sys
input = sys.stdin.readline
print = sys.stdout.write
n = int(input())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())
for i in sorted(nums):
    print(str(i) + '\n')