import sys, math

i = int(sys.stdin.readline())
for _ in range(i):
    n, m = map(int, sys.stdin.readline().split())
    N = m - n
    r_N = math.sqrt(N)
    N_int = math.trunc(r_N)
    if r_N == N_int: print(N_int * 2 - 1)
    else:
        if N > N_int * (N_int + 1):
            print(N_int * 2 + 1)
        else:
            print(N_int * 2)