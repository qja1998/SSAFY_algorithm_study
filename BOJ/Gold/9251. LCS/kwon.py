import bisect

s1 = input()
s2 = input()

dupli_set = set(s1) & set(s2)

dupli_s1 = ''
dupli_s2 = ''
for c1 in s1:
    if c1 not in dupli_set:
        continue
    dupli_s1 += c1

for c2 in s2:
    if c2 not in dupli_set:
        continue
    dupli_s2 += c2
# 하나를 dfs하면서 만들고 다른 문자열에서 인덱스 옮겨가면서 확인
def dfs(s, c):
    i2 = s2.find(c)
    if i2 == -1:
        return
    dfs(s[1:], s[0])
    dfs(s[2:], s[1])