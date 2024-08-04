import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

n = int(input())
cnt_list = [0] * (n + 1)
for i in range(2, n + 1):
    min_cnt= cnt_list[i - 1] + 1
    
    if i % 3 == 0:
        tmp = cnt_list[i // 3] + 1
        if tmp < min_cnt:
            min_cnt = tmp
        
    if i % 2 == 0:
        tmp = cnt_list[i // 2] + 1
        if tmp < min_cnt:
            min_cnt = tmp
    
    cnt_list[i] = min_cnt

print(cnt_list[-1])