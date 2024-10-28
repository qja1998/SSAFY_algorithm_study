import sys
sys.stdin = open('input.txt', 'r')

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def solve(ci, cj, dr):
    cnt = 0 # 청소한 공간 수
    while 1:
        # 현재 위치 청소
        arr[ci][cj] = 2
        cnt += 1

        # 왼쪽 방향 순서로 탐색, 청소 안 된 곳으로 이동
        flag = 1
        while flag == 1:
            # 왼쪽부터 네 방향 중 청소 안 된 곳이 있는 경우
            for nd in ((dr+3)%4, (dr+2)%4, (dr+1)%4, (dr%4)): # 왼쪽 회전
                ni, nj = ci + dx[nd], cj + dy[nd]
                if arr[ni][nj] == 0: # 청소가 안 된 곳이라면
                    ci, cj, dr = ni, nj, nd
                    flag = 0
                    break
            else: # 네 방향 모두 청소 안 된 곳이 없다면 후진
                bi, bj = ci-dx[dr], cj-dy[dr] # 후진 위치 계산
                if arr[bi][bj] == 1: # 벽이라면 종료
                    return cnt
                else: # 후진
                    ci, cj = bi, bj

N, M = map(int, input().split())
si, sj, dr = map(int, input(). split())
arr = [list(map(int, input().split())) for _ in range(N)]

res = solve(si, sj, dr)
print(res)