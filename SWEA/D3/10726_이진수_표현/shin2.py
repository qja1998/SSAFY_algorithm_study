T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    m = bin(M)[2:]
    if len(m) < N:
        print(f"#{tc} OFF")
    else:
        if m[-N:] == ('1'* N):
            print(f"#{tc} ON")
        else:
            print(f"#{tc} OFF")
