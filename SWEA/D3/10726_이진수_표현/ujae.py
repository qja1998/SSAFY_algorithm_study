T = int(input())
 
for test_case in range(1, T+1):
    n,m = map(int, input().split())
    n = (2**(n)) - 1
    if n & m == n:
        print(f'#{test_case} ON')
    else:
        print(f'#{test_case} OFF')