T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    candies = sorted(list(map(int, input().split())))
    result = float('inf')
    for i in range(N-K+1):
        result = min(result, candies[i+K-1] - candies[i])
    print(f"#{tc} {result}")
