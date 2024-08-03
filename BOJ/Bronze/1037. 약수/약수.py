n = int(input())
div = list(map(int, input().split()))
min, max = float('inf'), float('-inf')
for d in div:
    if min > d : min = d
    if max < d : max = d
print(min * max)
