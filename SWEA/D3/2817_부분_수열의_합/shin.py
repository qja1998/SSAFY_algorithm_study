def dfs(idx=0, num_sum=0):
    global result

    if num_sum == K:
        result += 1
        return

    if num_sum > K:
        return

    if idx == N:
        return

    dfs(idx + 1, num_sum + arr[idx])
    dfs(idx + 1, num_sum)


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0

    dfs()
    print(f"#{tc} {result}")
