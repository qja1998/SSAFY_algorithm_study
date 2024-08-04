n = int(input())
diff = []
pre = int(input())
for i in range(n-1):
    cur = int(input())
    diff.append(abs(cur - pre))

def gcd(a, b):
    while a % b != 0:
        r = a % b
        a = b
        b = r
    return b

gcd_num = diff[0]
for i in range(len(diff) - 1):
    gcd_num = gcd(gcd_num, diff[i + 1])
ans = []
for i in range(int(gcd_num ** 0.5), 1, -1):
    if gcd_num % i == 0:
        ans.insert(0, i)
        if gcd_num // i != i:
            ans.append(gcd_num // i)
ans.append(gcd_num)
for n in ans:
    print(n, end=' ')
