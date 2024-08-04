from collections import defaultdict

n, k = map(int, input().split())
p = list(map(int, input().split()))

d = defaultdict(int)

for num in p:
    d[num] += 1

i = 0
for key in sorted(d, reverse=True):
    for j in range(d[key]):
       ans = key
       i += 1
       if i == k:
            break
    if i == k:
        break
print(ans)
