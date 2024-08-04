import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))
target = int(sys.stdin.readline().rstrip())
result = 0

def counting_sort(array, max):
 
    counting_array = [0]*(max+1)
    for i in array:
        counting_array[i] += 1
 
    for i in range(max):
        counting_array[i+1] += counting_array[i]
 
    output_array = [-1]*len(array)
    
    for i in array:
        output_array[counting_array[i] -1] = i
        counting_array[i] -= 1
    return output_array

nums = counting_sort(nums, max(nums))

l, r = 0, n - 1
while l < r:
    tmp = nums[l] + nums[r]
    if tmp < target:
        l += 1
    elif tmp == target:
        result += 1
        l += 1
    else:
        r -= 1

print(result)