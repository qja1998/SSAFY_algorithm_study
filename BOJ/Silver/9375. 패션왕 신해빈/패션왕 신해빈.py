from collections import defaultdict
t = int(input())
for _ in range(t):
    d = defaultdict(int)
    n = int(input())
    for i in range(n):
        _, cat = input().split()
        d[cat] += 1
    ans = 1
    for cat in d:
        ans *= d[cat] + 1
    print(ans - 1)
    
