n, m = map(int, input().split())
cnt = 0
prime = [1] * (m - n + 1)
i = 2
while i ** 2 <= m:
    sqr = i ** 2
    j = n // sqr
    while sqr * j <= m:
        if sqr * j >= n and prime[sqr * j - n] == 1:
            prime[sqr * j - n] = 0
        j += 1
    i += 1
print(sum(prime))