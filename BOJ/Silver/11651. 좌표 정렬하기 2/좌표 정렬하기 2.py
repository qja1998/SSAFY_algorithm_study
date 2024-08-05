import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
cnt_list = [[] for i in range(200002)]
for _ in range(n):
    x, y = map(int, input().split())
    cnt_list[y + 100000].append(x)

for y, xs in enumerate(cnt_list):
    if xs:
        if len(xs) == 1:
            print(f"{xs[0]} {y - 100000}\n")
        else:
            for x in sorted(xs):
                print(f"{x} {y - 100000}\n")