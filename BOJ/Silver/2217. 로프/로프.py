n = int(input())
result = 0
cnt = 0
rope = []
for i in range(0, n):
    rope.append(int(input()))

rope.sort(reverse=True)
max_w = 0
for cnt, r in enumerate(rope):
    if max_w <= r * (cnt + 1):
        max_w = r * (cnt + 1)

print(max_w)
