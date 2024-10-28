N, K = map(int, input().split())

N += 1
K += 1

n = 0

while N * 2**n <= K:
    # print(N * 2**n, K)
    n += 1
# print(N * 2**n)
before_diff = K - N * 2**(n-1)
after_diff = N * 2**n - K
# print(before_diff, after_diff)
# print()
if before_diff < after_diff:
    n -= 1
    remain = before_diff
else:
    remain = after_diff


# remain = K % (N * 2^n)
# print(n, remain)
# print()

result = n

while N >= 0:
    # print(remain)
    # print(N, 2**N, remain // 2**N)
    result += remain // 2**N
    remain %= 2**N
    N -= 1
    # print(result)

print(result)