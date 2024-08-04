n = int(input())

def fibb(n):
    if n == 0: return 0
    elif n == 1: return 1
    return fibb(n - 1) + fibb(n - 2)

print(fibb(n))
