from collections import defaultdict
import sys
input = sys.stdin.readline
n = int(input())
mean = 0
d = defaultdict(int)
num_range = 0
min, max = float('inf'), -float('inf')
for _ in range(n):
    num = int(input())
    mean += num
    d[num] += 1
    if num < min:
        min = num
    if num > max:
        max = num
        
cnt = 0
min1, min2 = float('inf'), float('inf')
max_cnt = -float('inf')
for num in sorted(d):
    num_cnt = d[num]
    for _ in range(num_cnt):
        if cnt == n // 2:
            mid = num
        cnt += 1
    if max_cnt < num_cnt:
        max_cnt = num_cnt
        min1 = num
        min2 = float('inf')
    elif max_cnt == num_cnt:
        if min1 > num:
            min1 = num
            min2 = min1
        elif min1 <= num < min2:
            min2 = num
if min2 == float('inf'):
    freq = min1
else:
    freq = min2


mean = int(round(mean / n, 0))
num_range = max - min

print(mean)
print(mid)
print(freq)
print(num_range)
