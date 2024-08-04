import sys
input = sys.stdin.readline

num = input().strip()
cnt_dict = {str(n):0 for n in range(9, -1, -1)}
for i in num:
    cnt_dict[i] += 1
ans = ''
for i in cnt_dict:
    for _ in range(cnt_dict[i]):
        ans += i

print(ans)