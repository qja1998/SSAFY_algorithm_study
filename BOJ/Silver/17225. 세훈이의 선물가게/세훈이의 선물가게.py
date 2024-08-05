import sys
from collections import defaultdict

sm, js, n = map(int, sys.stdin.readline().split())

time_dic = defaultdict(list)
cnt_b = 0
cnt_r = 0
sorted_k = []

for i in range(n):
    t, c, m = sys.stdin.readline().split()
    if c == 'B':
        if sm == 0:
            speed = 0
        else:
            speed = sm
        cnt_b += int(m)
        
    elif c == 'R':
        if js == 0:
            speed = 0
        else:
            speed = js
        cnt_r += int(m)
            
    for j in range(1, int(m)+1):
        tmp = int(t) + j * speed
        time_dic[tmp].append(c)
        if tmp not in sorted_k:
            sorted_k.append(tmp)
            

sorted_k.sort()

time = 1

list_b = []
list_r = []

for t in sorted_k:
    for c in sorted(time_dic[t]):
        if c == 'B':
            list_b.append(time)
        else:
            list_r.append(time)
        time += 1

print(cnt_b)
for i in list_b:
    print(i, end=' ')
print('')
print(cnt_r)
for i in list_r:
    print(i, end=' ')