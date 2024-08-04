from math import factorial as fac
n, k = map(int, input().split())
if k < 0 or k > n:
    print(0)
else:
    print(fac(n) // (fac(k) * fac(n - k)))
