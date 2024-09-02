T = int(input())
for ts in range(1, T+1):
    N = int(input())
    List = []
    sb = []
    count = 0
    for _ in range(N):
        List.append(input())
    for i in range(len(List)):
        if N//2 >= i:
            sb.append(List[i][(N//2)-i:(N//2)+i+1])
        else:
            sb.append(List[i][i-(N//2+N):(N//2)-i])
    for i in range(len(sb)):
        for j in range(len(sb[i])):
            count += int(sb[i][j])
    print(f"#{ts} {count}")
