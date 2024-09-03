TC = int(input())

for t in range(1, TC+1):
    N, M = map(int, input().split())

    things = [list(map(int, input().split())) for _ in range(M)]

    dp = [0] * (N+1)

    for s, p in things:
        for i in range(N-s+1):
            if dp[i] < dp[s+i]+p:
                dp[i] = dp[s+i]+p

    print(f"#{t} {max(dp)}")