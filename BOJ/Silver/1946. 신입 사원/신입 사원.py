import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    p_cnt = [0] * (n + 1)
    p_cnt2 = [0] * (n + 1)
    for _ in range(n):
        s1, s2 = map(int, input().split())
        p_cnt[s1] = (s1, s2)
        p_cnt2[s2] = (s1, s2)
    top1 = p_cnt[1][1]
    top2 = p_cnt2[1][0]
    
    cnt = 1
    best_s1, best_s2 = p_cnt[1]
    for s1, s2 in p_cnt[2:]:
        if best_s2 > s2:
            cnt += 1
            best_s2 = s2
    print(cnt)
