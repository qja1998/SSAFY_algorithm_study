# # import sys
# from itertools import combinations
# # sys.stdin = open(r"C:\Users\SSAFY\Downloads\input (1).txt", "r")

# TC = int(input())

# INF = float('inf')

# for t in range(1, TC+1):
#     n = int(input())

#     positions = [tuple(map(int, input().split())) for _ in range(n)]

#     positions.sort(key=lambda x: x[0]**2 + x[1]**2)

#     selected_pos = combinations(positions, n//2)

#     min_vec = INF
#     for pos_list in selected_pos:
#         pos_list2 = list(set(positions)-set(pos_list))

#         sum_x, sum_y = 0, 0

#         for (x1, y1), (x2, y2) in zip(pos_list, pos_list2):
#             sum_x += x1 - x2
#             sum_y += y1 - y2

#         min_vec = min(min_vec, sum_x**2 + sum_y**2)

    
#     print(f"#{t} {min_vec}")









# 100개 中 23개

# import sys
# sys.stdin = open(r'C:\Users\SSAFY\Downloads\input.txt', 'r')

import itertools

def calcul_vect(a, b):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    vectx = ax - bx
    vecty = ay - by
    return vectx, vecty

def match_how(vect_li, check_li):
    tmp_chk = check_li[:]
    for i in range(vect_li):
        if check_li[vect_li[j][0]]:
            continue
        if check_li[vect_li[j][1]]:
            continue
        tmp_chk[vect_li[j][0]] = True
        tmp_chk[vect_li[j][1]] = True
        match_how(vect_li[i:], tmp_chk)


# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mapli = [list(map(int, input().split())) for _ in range(N)]

    # 매칭할 수 있는 조합 찾기
    match = list(itertools.combinations([i for i in range(N)], 2))

    #
    # vectx = []
    # vecty = []
    vect_li = []
    min_vect = 99999999999
    # xsum_vect = 0
    # ysum_vect = 0
    # check_li = [False] * N

    # 두 지렁이 사이의 벡터 구하기
    for i in match:
        cal = [i[0], i[1], calcul_vect(mapli[i[0]], mapli[i[1]])]
        cal2 = [i[1], i[0], calcul_vect(mapli[i[1]], mapli[i[0]])]
        if cal[2] == (0, 0):
            continue
        vect_li.append(cal)
        vect_li.append(cal2)
        # print(vect_li)

    # 어떤 조합이 최선일지 검정
    for i in range(len(vect_li)):
        xsum_vect = 0
        ysum_vect = 0
        check_li = [False] * N

        visited = []
        for j in range(i, len(vect_li)):
            # 이미 짝이 있는 지렁이면 패스
            if check_li[vect_li[j][0]]:
                continue
            if check_li[vect_li[j][1]]:
                continue
            visited.append(vect_li[j][:2])
            # 이번 지렁이 짝 있다고 표시
            check_li[vect_li[j][0]] = True
            check_li[vect_li[j][1]] = True
            # 전체 벡터에 지금 벡터 더해주기
            xsum_vect += vect_li[j][2][0]
            ysum_vect += vect_li[j][2][1]
            # print(check_li, xsum_vect, ysum_vect)

        for j in range(i):
            # 이미 짝이 있는 지렁이면 패스
            if check_li[vect_li[j][0]]:
                continue
            if check_li[vect_li[j][1]]:
                continue
            visited.append(vect_li[j][:2])
            # 이번 지렁이 짝 있다고 표시
            check_li[vect_li[j][0]] = True
            check_li[vect_li[j][1]] = True
            # 전체 벡터에 지금 벡터 더해주기
            xsum_vect += vect_li[j][2][0]
            ysum_vect += vect_li[j][2][1]
            # print(check_li, xsum_vect, ysum_vect)

        print(visited)
        
        # 전체 벡터의 최소값 찾기
        this_vect = xsum_vect * xsum_vect + ysum_vect * ysum_vect
        min_vect = min(min_vect, this_vect)
        # print(this_vect, min_vect)

    # 정답 출력
    print(f'#{tc} {min_vect}')
