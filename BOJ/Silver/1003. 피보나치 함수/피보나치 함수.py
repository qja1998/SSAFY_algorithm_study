n = int(input())

memo1 = {}
memo2 = {}

def fib(n):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    
    if n in memo1:
        zero = memo1[n]
    
    if n in memo2:
        one = memo2[n]
    else:
        zero1, one1 = fib(n - 1)
        zero2, one2 = fib(n - 2)
        zero = zero1 + zero2
        one = one1 + one2
        memo1[n] = zero
        memo2[n] = one
    return zero, one

for _ in range(n):
    num = int(input())
    print(*fib(num), sep=' ')