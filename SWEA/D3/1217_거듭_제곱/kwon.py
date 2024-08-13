def exp(n, m):
    if m == 0:
        return 1
    return exp(n, m - 1) * n

for _ in range(10):
    t = int(input())

    n, m = map(int, input().split())
    print(f"#{t} {exp(n, m)}")