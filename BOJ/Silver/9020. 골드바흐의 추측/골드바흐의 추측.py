import sys

input = sys.stdin.readline

prime_num = [True] * 10001
prime_num[0], prime_num[1] = False, False

for i in range(2, 10001):
    if prime_num[i]:
        j = 2
        while i * j <= 10000:
            prime_num[i * j] = False
            j += 1
        
for _ in range(int(input())):
    n = int(input())
    a, b = n // 2, n // 2
    while not (prime_num[a] and prime_num[b]):
        a -= 1
        b += 1
    print(a, b)