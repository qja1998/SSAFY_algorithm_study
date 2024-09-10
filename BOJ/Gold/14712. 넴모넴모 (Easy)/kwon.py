def fill_nemo(d=0):
    global cnt
    if N*M == d:
        cnt += 1
        return
    
    y = d // M + 1
    x = d  % M + 1

    # 사각형이 완성 안되는 경우
    if matrix[y-1][x] == 0 or matrix[y-1][x-1] == 0 or matrix[y][x-1] == 0:
        # 다음 위치에 네모 생성
        matrix[y][x] = 1
        fill_nemo(d+1)
        matrix[y][x] = 0

    # 다음 위치에 네모 생성 X
    fill_nemo(d+1)
    

N, M = map(int, input().split())

matrix = [[0]*(M+1) for _ in range(N+1)]

cnt = 0
fill_nemo()

print(cnt)