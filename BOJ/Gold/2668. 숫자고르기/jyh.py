# N = int(input())
# graph = {}
# for i in range(1, N+1):
#     x = int(input())
#     graph[i] = x
# # print(graph)
#
# visited = [False] * (N + 1)
# keep = []
#
# for i in range(1, N+1):
#     visited[i] = True
#     this = graph[i]
#     keep.append(this)
#     temp = [i, this]
#     a = len(temp)
#     while True:
#         for j in range(1, N+1):
#             if not visited[j]:
#                 that = graph[j]
#                 if that in temp and j in temp:
#                     visited[j] = True
#                     keep.append(that)
#         b = len(keep)
#         if a != b:
#             keep.pop()
#         break
#
# print(len(keep))
# for i in sorted(keep):
#     print(i)


# 일대일 매핑. 두개가 한 쌍일때만 읽음.
N = int(input())
graph = {}
for i in range(1, N+1):
    x = int(input())
    graph[i] = x
# print(graph)

keep = []
temp = []
for i in range(1, N+1):
    this = graph[i]
    temp.append(i)
    temp.append(this)
    for j in range(1, N+1):
        that = graph[j]
        if that in temp and j in temp:
            keep.extend((that, j))
            break

print(len(keep))
for i in sorted(keep):
    print(i)