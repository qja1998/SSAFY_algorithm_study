from collections import defaultdict
word = input().upper()

counter = defaultdict(int)

max_cnt = 0
max_alpha = ''
same_chk = False

for a in word:
    counter[a] += 1
    if counter[a] > max_cnt:
        max_cnt = counter[a]
        max_alpha = a
        same_chk = False
    elif counter[a] == max_cnt:
        same_chk = True

if same_chk:
    print('?')
else:
    print(max_alpha)