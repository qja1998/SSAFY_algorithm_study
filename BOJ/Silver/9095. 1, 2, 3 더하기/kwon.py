T = int(input())

def dfs(n):
    global cnt
    if n == 0:
        cnt += 1
    if n < 0:
        return

    dfs(n - 1)
    dfs(n - 2)
    dfs(n - 3)

for _ in range(T):
    n = int(input())

    cnt = 0
    dfs(n)

    print(cnt)