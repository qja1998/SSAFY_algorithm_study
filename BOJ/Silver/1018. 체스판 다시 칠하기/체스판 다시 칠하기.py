n, m = map(int, input().split())
ONE_LAYER = "WB" * (m // 2 + 1)

def repainting(layer, start):
    cnt = 0
    check = [0] * len(layer)
    for i, l in enumerate(layer):
        if ONE_LAYER[start] != l:
            check[i] = 1
        start += 1
    return check

cnts1, cnts2 = [0] * n, [0] * n
start1, start2 = 0, 1

for i in range(n):
    layer = input()
    cnts1[i] = repainting(layer, start1)
    cnts2[i] = repainting(layer, start2)
    start1, start2 = start2, start1

ans = float('inf')
for i in range(n - 7):
    tmp1 = cnts1[i:i+8]
    tmp2 = cnts2[i:i+8]
    for j in range(m - 7):
        s1, s2 = 0, 0
        for i, t in enumerate(tmp1):
            s1 += sum(t[j:j+8])
            s2 += sum(tmp2[i][j:j+8])
        if s1 < ans:
            ans = s1
        if s2 < ans:
            ans = s2
print(ans)
            
