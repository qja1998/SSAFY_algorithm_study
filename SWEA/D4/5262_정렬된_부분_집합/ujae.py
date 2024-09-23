T = int(input())
 
for test_case in range(1, T+1):
    num_list = list(map(int, input().split()))
    n = len(num_list)
 
    dp = [1] * n
 
    for i in range(1, n):
        for j in range(0, i):
            if num_list[j] < num_list[i]:
                dp[i] = max(dp[i], dp[j] + 1)
 
    print(f'#{test_case} {max(dp)}')
