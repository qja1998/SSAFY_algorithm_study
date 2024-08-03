n, m = map(int, input().split())
d, b = set(), []
for _ in range(n):
    d.add(input())
for _ in range(m):
    name = input()
    if name in d:
        b.append(name)
print(len(b))
for n in sorted(b):
    print(n)
