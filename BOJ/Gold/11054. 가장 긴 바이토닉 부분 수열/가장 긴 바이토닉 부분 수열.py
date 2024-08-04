import sys
from urllib.parse import MAX_CACHE_SIZE
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

memo = {}

def bitonic(i: int, num: int, left: bool, right: bool) -> int:
    if (i, left, right) in memo:
        return memo[(i, left, right)]
   
    max_l, max_r = 1, 1
   
    if num == 1:
        memo[(i, left, right)] = 1
        return 1
    if left:
        for j in range(0, i):
            conp_n = nums[j]
            if num > conp_n:
                left_num = bitonic(j, conp_n, True, False) + 1
                if max_l < left_num:
                    max_l = left_num
        memo[(i, left, right)] = max_l
    if right:
        for j in range(i+1, n):
            conp_n = nums[j]
            if num > conp_n:
                right_num = bitonic(j, conp_n, False, True) + 1
                if max_r < right_num:
                    max_r = right_num
        memo[(i, left, right)] = max_r
    return max_l + max_r - 1

ans = 0
for i, num in enumerate(nums):
    out = bitonic(i, num, True, True)
    if ans < out:
        ans = out
print(ans)