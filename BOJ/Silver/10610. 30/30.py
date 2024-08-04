import sys
nums = str(sys.stdin.readline().strip())
if '0' not in nums:
    print(-1)
else:
    l = [0] * (int(max(nums)) + 1)
    s = ''
    sum = 0
    for i in nums:
        l[int(i)] += 1
    for i in range(len(l)-1, 0, -1):
        s += str(i) * l[i]
        sum += i * l[i]
    if sum % 3 == 0: print(int(s) * (10 ** l[0]))
    else: print(-1)