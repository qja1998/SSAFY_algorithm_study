n = int(input())
meetings = []

for _ in range(n):
    s, f = map(int, input().split())
    meetings.append((s, f))

meetings.sort(key=lambda x: (x[1], x[0]))

cur = 0
cnt = 0
for s, f in meetings:
    if cur <= s:
        cur = f
        cnt += 1
print(cnt)
