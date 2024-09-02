def power(n, m):
    if m > 0:
        return n * power(n, m-1)
    else:
        return 1

for _ in range(1, 11):
    test_case = int(input())
    N, M = map(int, input().split())
    print(f"#{test_case} {power(N, M)}")
