import sys
sys.stdin = open('input.txt', 'r')

# N * N 칸
# 포자 M개 => 최대 K개 연결된 칸에 버섯자라게 함, 0인 곳에만 심을 수 있음
# 버섯이 자랄 수 있는 칸은 0, 자랄 수 없는 칸은 1 => 모든 칸이 0이 되어야 POSSIBLE

from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


# 버섯 퍼뜨리기
def bfs(i, j):
    spore_cnt = 1
    queue = deque()
    queue.append((i, j))
    arr[i][j] = 1 # 버섯 심기
    while queue:
        ci, cj = queue.popleft()
        for dx, dy in dxy:
            ni, nj = ci + dx, cj + dy
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                # 어떤 모양으로 퍼지든 일단 개수가 중요
                queue.append((ni, nj))
                arr[ni][nj] = 1  # 버섯 심기
                spore_cnt += 1
                if spore_cnt == K:
                    return


def mushroom():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1

    # 버섯 포자를 하나 이상 꼭 사용해야함 !!! 이 조건을 안 넣으면 틀림
    if cnt == 0:
        print('IMPOSSIBLE')
        return

    # 포자 개수가 심을 수 있는 공간보다 적으면 버섯 못 심음
    if M < cnt:
        print('IMPOSSIBLE')
        return

    # 포자 개수가 심을 수 있는 공간보다 많은데 1만큼만 퍼진다면
    # 공간만큼 사용하고 남은 걸 출력하면 됨
    if K == 1:
        print('POSSIBLE')
        print(M - cnt)
        return

    # 포자 개수가 심을 수 있는 공간보다 많고 K만큼 퍼진다면
    # bfs로 버섯 심어보자
    spore_used = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                bfs(i, j)
                spore_used += 1
                if spore_used > M:
                    print('IMPOSSIBLE')
                    return

    print('POSSIBLE')
    print(M - spore_used)


mushroom()

'''
from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(i, j):
    spore_cnt = 0
    queue = deque()
    queue.append((i, j))
    arr[i][j] = 1 # 버섯 심기
    while queue:
        for dx, dy in dxy:
            ci, cj = queue.popleft()
            ni, nj = ci + dx, cj + dy
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                # 어떤 모양으로 퍼지든 일단 개수가 중요
                queue.append((ni, nj))
                arr[ni][nj] = 1 # 버섯 심기
                spore_cnt += 1
                if spore_cnt == K:
                    break


def mushroom():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 0

    if M >= cnt and K == 1:
        print(M - cnt)
    elif M < cnt:
        print('IMPOSSIBLE')
    else:
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    bfs(i, j)

    if not 1 in arr:
        print('POSSIBLE')
        print(M - cnt)


mushroom()
'''