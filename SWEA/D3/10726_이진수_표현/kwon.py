# 비트 연산
test_case = int(input())

for t in range(test_case):
    n, m = map(int, input().split())
    bit_n = 2 ** n - 1
    
    if bit_n & m == bit_n:
        print(f"#{t+1} ON")
    else:
        print(f"#{t+1} OFF")

# 단순 반복문
test_case = int(input())

def chk_n_bits(n, m):
    for _ in range(n):
        if m % 2 == 0:
            return False
        m //=2
    return True

for t in range(test_case):
    n, m = map(int, input().split())
    
    if chk_n_bits(n, m):
        print(f"#{t+1} ON")
    else:
        print(f"#{t+1} OFF")