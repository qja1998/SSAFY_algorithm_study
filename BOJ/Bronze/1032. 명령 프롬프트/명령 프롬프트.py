import sys

n = int(sys.stdin.readline())

sen = list(sys.stdin.readline().strip())
length = len(sen)

for _ in range(n-1):
    tmp = sys.stdin.readline().strip()
    for i in range(length):
        if sen[i] != tmp[i]:
            sen[i] = '?'

print(''.join(sen))