import sys

n,m = map(int, sys.stdin.readline().split())
list = []
dict = {}
for i in range(n + m):
    tmp = sys.stdin.readline().strip()
    if i < n:
        list.append(tmp)
        dict[tmp] = i + 1
    else:
        if tmp.isdigit():
            print(list[int(tmp) - 1])
        else:
            print(dict[tmp])