n, k = map(int, input().split())

lights = list(map(int, input().split()))
cnt = 0

b = [lights[i] ^ lights[i-1] for i in range(1, n)]
b.insert(0, 0 ^ lights[0])

i = 0

while i < n-k:
    if b[i]:
        b[i] = b[i] ^ 1
        b[i+k] = b[i+k] ^ 1
        cnt += 1
    i += 1

c = [b[0]]
for i in range(1, len(b)):
    c.append(c[i - 1] ^ b[i])
s = sum(c)

if s == k:
    print(cnt + 1)
elif s == 0:
    print(cnt)
else:
    print('Insomnia')