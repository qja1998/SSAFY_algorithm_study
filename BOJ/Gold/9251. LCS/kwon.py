s1 = input()
s2 = input()

pd = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]

for y, c2 in enumerate(s2, start=1):
    for x, c1 in enumerate(s1, start=1):
        if c1 != c2:
            pd[y][x] = max(pd[y - 1][x], pd[y][x - 1])
            continue

        pd[y][x] = pd[y-1][x-1] + 1

print(max(map(max, pd)))


# s1 = input()
# s2 = input()

# dupli_set = set(s1) & set(s2)

# dupli_s1 = ''
# dupli_s2 = ''
# for c1 in s1:
#     if c1 not in dupli_set:
#         continue
#     dupli_s1 += c1

# for c2 in s2:
#     if c2 not in dupli_set:
#         continue
#     dupli_s2 += c2

# max_len = 0

# # 하나를 dfs하면서 만들고 다른 문자열에서 인덱스 옮겨가면서 확인
# def dfs(s1, s2, c, i2=0, cnt=0, visited=[]):
#     global max_len

#     if len(s1) == 0 or len(s2) == 0:
#         max_len = max(max_len, cnt)
#         return cnt
    
#     if len(s1) > 1:
#         dfs(s1[1:], s2, s1[0], i2, cnt, visited)

#     i2 = s2.find(c)

#     if i2 == -1:
#         max_len = max(max_len, cnt)
#         return cnt
    
#     dfs(s1[1:], s2[i2+1:], s1[0], i2, cnt+1, visited+[c])

# dfs(s1, s2, s1[0])
# # dfs(s2, s1, s2[0])
# print(max_len)