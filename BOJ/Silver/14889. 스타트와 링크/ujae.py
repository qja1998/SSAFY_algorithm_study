#-----------------------------0트-------------------------------------------------
#-----------------------------0트-------------------------------------------------
#----------------------------_0트-------------------------------------------------
#-----------------------------0트-------------------------------------------------
#-----------------------------0트-------------------------------------------------
#-----------------------------0트-------------------------------------------------
#-----------------------------0트-------------------------------------------------

N = int(input())
ability_info = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
result = 40000
result_list = []

def dfs(len, count):
    global result
    result1 = 0
    result2 = 0
    if len == N//2:
        for i in range(N):
            for j in range(i+1, N):
                if i != j:
                    if visited[i] and visited[j]:
                        result1 += (ability_info[i][j] + ability_info[j][i])
                    elif not visited[i] and not visited[j]:
                        result2 += (ability_info[i][j] + ability_info[j][i])

        result = min(result, abs(result1- result2))
        result_list.append(result)
        return
    else:
        for m in range(count, N):
            if not visited[m]:
                visited[m] = True
                dfs(len+1, m+1)
                visited[m] = False

dfs(0, 0)
print(min(result_list))

#-----------------------------1트-------------------------------------------------
#-----------------------------1트-------------------------------------------------
#----------------------------_1트-------------------------------------------------
#-----------------------------1트-------------------------------------------------
#-----------------------------1트-------------------------------------------------
#-----------------------------1트-------------------------------------------------
#-----------------------------1트-------------------------------------------------

# N = int(input())
# ability_info = [list(map(int, input().split())) for _ in range(N)]
# visited = [False for _ in range(N)]
# result = 40000

# def dfs(len, count):
#     global result
#     result1 = 0
#     result2 = 0
#     if len == N//2:
#         for i in range(N):
#             for j in range(i+1, N):
#                 if i != j:
#                     if visited[i] and visited[j]:
#                         result1 += (ability_info[i][j] + ability_info[j][i])
#                     elif not visited[i] and not visited[j]:
#                         result2 += (ability_info[i][j] + ability_info[j][i])

#         result = min(result, abs(result1- result2))
#         return
#     else:
#         for m in range(count, N):
#             if not visited[m]:
#                 visited[m] = True
#                 dfs(len+1, count+1)
#                 visited[m] = False

# dfs(0, 0)
# print(result)

#-----------------------------2트-------------------------------------------------
#-----------------------------2트-------------------------------------------------
#----------------------------_2트-------------------------------------------------
#-----------------------------2트-------------------------------------------------
#-----------------------------2트-------------------------------------------------
#-----------------------------2트-------------------------------------------------
#-----------------------------2트-------------------------------------------------

# from itertools import combinations
#
# N = int(input())
# ability_info = [list(map(int, input().split())) for _ in range(N)]
# visited = [False for _ in range(N)]
# result = 40000
# result_list = []
#
# for i in combinations(range(N), N//2):
#     result1 = 0
#     result2 = 0
#     for num1 in range(N):
#         for num2 in range(num1+1, N):
#             if num1 != num2:
#                 if num1 in i and num2 in i:
#                     result1 += ability_info[num1][num2] + ability_info[num2][num1]
#                 elif num1 not in i and num2 not in i:
#                     result2 += ability_info[num1][num2] + ability_info[num2][num1]
#     result = min(result, abs(result1- result2))
#
# print(result)
#-----------------------------3트-------------------------------------------------
#-----------------------------3트-------------------------------------------------
#-----------------------------3트-------------------------------------------------
#-----------------------------3트-------------------------------------------------
#-----------------------------3트-------------------------------------------------
#-----------------------------3트-------------------------------------------------
#-----------------------------3트-------------------------------------------------

# import sys
#
# input = sys.stdin.readline
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# visited = [False for _ in range(N)]
# INF = 2147000000
# res = INF
#
# def DFS(L, idx):
#     global res
#     if L == N // 2:
#         A = 0
#         B = 0
#         for i in range(N):
#             for j in range(N):
#                 if visited[i] and visited[j]:
#                     A += board[i][j]
#                 elif not visited[i] and not visited[j]:
#                     B += board[i][j]
#         res = min(res, abs(A - B))
#         return
#     for i in range(idx, N):
#         if not visited[i]:
#             visited[i] = True
#             DFS(L + 1, i + 1)
#             visited[i] = False
#
#
# DFS(0, 0)
# print(res)
#-----------------------------4트-------------------------------------------------
#-----------------------------4트-------------------------------------------------
#----------------------------_4트-------------------------------------------------
#-----------------------------4트-------------------------------------------------
#-----------------------------4트-------------------------------------------------
#-----------------------------4트-------------------------------------------------
#-----------------------------4트-------------------------------------------------

# import sys

# input = sys.stdin.readline

# N = int(input())
# ability_info = [list(map(int, input().split())) for _ in range(N)]
# visited = [False for _ in range(N)]
# result = 2147000000

# def dfs(len, count):
#     global result
#     result1 = 0
#     result2 = 0
#     if len == N//2:
#         for i in range(N):
#             for j in range(N):
#                 if visited[i] and visited[j]:
#                     result1 += ability_info[i][j]
#                 elif not visited[i] and not visited[j]:
#                     result2 += ability_info[i][j]

#         result = min(result, abs(result1- result2))
#         return
#     else:
#         for m in range(count, N):
#             if not visited[m]:
#                 visited[m] = True
#                 dfs(len+1, m+1)
#                 visited[m] = False

# dfs(0, 0)
# print(result)





# import sys

# input = sys.stdin.readline
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# visited = [False for _ in range(N)]
# INF = 2147000000
# res = INF

# def DFS(L, idx):
#     global res
#     if L == N // 2:
#         A = 0
#         B = 0
#         for i in range(N):
#             for j in range(N):
#                 if visited[i] and visited[j]:
#                     A += board[i][j]
#                 elif not visited[i] and not visited[j]:
#                     B += board[i][j]
#         res = min(res, abs(A - B))
#         return
#     for i in range(idx, N):
#         if not visited[i]:
#             visited[i] = True
#             DFS(L + 1, i + 1)
#             visited[i] = False


# DFS(0, 0)
# print(res)
