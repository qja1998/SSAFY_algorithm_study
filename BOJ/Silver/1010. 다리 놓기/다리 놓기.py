from math import factorial as fac
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(fac(m) // (fac(n) * fac(m - n)))
