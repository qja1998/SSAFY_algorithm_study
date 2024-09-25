def dfs(e_num):
    global arr
    arr[e_num] = -2
    for i in range(N):
        if arr[i] == e_num:
            dfs(i)


N = int(input())
arr = list(map(int, input().split()))
erase_N = int(input())
result = 0

dfs(erase_N)
for idx in range(N):
    if arr[idx] != -2 and idx not in arr:
        result += 1

print(result)
