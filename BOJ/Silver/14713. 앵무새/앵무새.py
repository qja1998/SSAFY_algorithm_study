n = int(input())
parrots = []
for _ in range(n):
    parrots.append(input().split())

sen = input().split()
length = len(sen)

for c in sen:
    possible = False
    for p in parrots:
        if p and p[0] == c:
            p.pop(0)
            possible = True
            break
    if not possible:
        break
for p in parrots:
    if p:
        possible = False
        break
print("Possible" if possible else "Impossible")