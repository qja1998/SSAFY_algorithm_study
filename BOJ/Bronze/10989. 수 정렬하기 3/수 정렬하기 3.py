import sys
from collections import defaultdict
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = []
d = defaultdict(int)

for _ in range(n):
    d[int(input())] += 1

for num in sorted(d):
    for _ in range(d[num]):
        print(f'{str(num)}\n')
