A = list(map(int,input().split()))
b = [1, 1, 2, 2, 2, 8]
ans = [0] * 6
for i in range(6):
    ans[i] = b[i] - A[i]
for n in ans:
    print(n, end=' ')
