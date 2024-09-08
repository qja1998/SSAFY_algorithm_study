from collections import defaultdict
from itertools import permutations

def search_wieght(mass_p, mass_sum, i=0, right=0, left=0):
    global cnt
    
    if mass_sum // 2 < left:
        cnt += 2 ** (n-i)
        return
    
    if i == n:
        cnt += 1
        return

    # 왼쪽에 추가
    search_wieght(mass_p, mass_sum, i+1, right, left+mass_p[i])
    
    # 오른쪽이 큼
    if right + mass_p[i] > left:
        return
    
    # 오른쪽에 추가
    search_wieght(mass_p, mass_sum, i+1, right+mass_p[i], left)


test_case = int(input())

for t in range(test_case):
    n = int(input())
    mass_list = list(map(int, input().split()))

    cnt = 0
    memo = defaultdict(int)
    mass_permutations = permutations(mass_list)

    for mass_p in mass_permutations:
        search_wieght(mass_p, sum(mass_p))
    print(f"#{t+1} {cnt}")