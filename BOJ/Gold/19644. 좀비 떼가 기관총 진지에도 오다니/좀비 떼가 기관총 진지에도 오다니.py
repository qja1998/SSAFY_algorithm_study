import sys
l = int(sys.stdin.readline().strip())
ml, mk = map(int, sys.stdin.readline().strip().split())
c = int(sys.stdin.readline().strip())
c_check, c_cnt = [False] * l, 0
live = True

for right in range(l):
    z = int(sys.stdin.readline().strip())
    
    if right > ml - 2: left = right - ml + 1
    else: left = 0
    
    damage = (right - left + 1 - c_cnt) * mk
    
    if damage < z:
        c_check[right] = True
        if c:
            c -= 1
            c_cnt += 1
        else:
            live = False
            print("NO")
            break
        
    if right - ml + 2 >= 0 and c_check[left]: c_cnt -= 1
    if c_cnt < 0: c_cnt = 0
    
if live: print("YES")