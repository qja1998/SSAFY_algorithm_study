T = int(input())
 
for test_case in range(1, T+1):
    N = int(input())
 
    tile_list = [0, 1, 3, 6]
 
    for i in range(4, N+1):
        tile_list.append(tile_list[i-1]+ 2*tile_list[i-2] + tile_list[i-3])
 
    print(f'#{test_case} {tile_list[N]}')
