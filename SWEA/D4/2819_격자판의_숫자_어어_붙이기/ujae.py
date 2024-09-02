def dfs_num_list(i, j, num_length):
    if len(num_length) == 7:
        result.append(num_length)
        return
    else:
        for x, y in move:
            xi, yi = i+x, j+y
            if 0<=xi<4 and 0<=yi<4:
                dfs_num_list(xi,yi,num_length+num_list[xi][yi])
 
move = [[-1,0],[1,0],[0,-1],[0,1]]
 
T = int(input())
 
for test_case in range(1,T+1):
    num_list = [input().split() for _ in range(4)]
    result = []
 
    for i in range(len(num_list)):
        for j in range(len(num_list)):
            dfs_num_list(i,j,num_list[i][j])
 
    print(f'#{test_case} {len(set(result))}')
