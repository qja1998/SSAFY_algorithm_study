import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
cnt_list = [[] for i in range(200002)]
for _ in range(n):
    x, y = map(int, input().split())
    cnt_list[x + 100000].append(y)

for x, ys in enumerate(cnt_list):
    if ys:
        if len(ys) == 1:
            print(f"{x - 100000} {ys[0]}\n")
        else:
            for y in sorted(ys):
                print(f"{x - 100000} {y}\n")