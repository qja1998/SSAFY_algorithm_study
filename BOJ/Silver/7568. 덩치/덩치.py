n = int(input())
l = []
cnt = [1] * n
for _ in range(n):
    l.append(tuple(map(int, input().split())))

for i in range(n):
    for j in range(i+1, n):
        p1, p2 = l[i], l[j]
        if p1[0] > p2[0] and p1[1] > p2[1]:
            cnt[j] += 1
        elif p1[0] < p2[0] and p1[1] < p2[1]:
            cnt[i] += 1
print(' '.join(map(str, cnt)))
