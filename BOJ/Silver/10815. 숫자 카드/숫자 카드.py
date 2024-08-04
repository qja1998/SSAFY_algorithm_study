import sys
print = sys.stdout.write

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in cards: print('1 ')
    else: print('0 ')
