import sys
from collections import Counter
print = sys.stdout.write

n = int(input())
cards = Counter(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in cards: print(f"{cards[num]} ")
    else: print("0 ")
