T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    bit = (1 << N) - 1
    if (M & bit) == bit:
        print(f"#{tc} ON")
    else:
        print(f"#{tc} OFF")
