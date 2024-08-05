import sys
sys.setrecursionlimit(10000)

n = int(input())

def sugar(n, cnt):
    if n == 0:
        return cnt
    if n >= 5:
        five = sugar(n - 5, cnt + 1)
        if five > 0:
            return five
    if n >= 3:
        three = sugar(n - 3, cnt + 1)
        if three > 0:
            return three
    return -1

print(sugar(n, 0))