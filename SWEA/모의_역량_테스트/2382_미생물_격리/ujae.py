T = int(input())
 
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
 
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    virus_info = [list(map(int, input().split())) for _ in range(K)]
 
    for _ in range(M):
        # tmp = []
        new_positions = {}
        for i in range(len(virus_info)):
            virus_info[i] = [virus_info[i][0]+move[virus_info[i][3]-1][0], virus_info[i][1]+move[virus_info[i][3]-1][1], virus_info[i][2], virus_info[i][3]]
            if not 1 <= virus_info[i][0] < N-1:
                if virus_info[i][3] == 1:
                    virus_info[i][3] = 2
                    virus_info[i][2] = int(virus_info[i][2]/2)
                else:
                    virus_info[i][3] = 1
                    virus_info[i][2] = int(virus_info[i][2]/2)
 
            if not 1 <= virus_info[i][1] < N-1:
                if virus_info[i][3] == 3:
                    virus_info[i][3] = 4
                    virus_info[i][2] = int(virus_info[i][2]/2)
                else:
                    virus_info[i][3] = 3
                    virus_info[i][2] = int(virus_info[i][2]/2)
 
            # 새 위치 저장
            if (virus_info[i][0], virus_info[i][1]) not in new_positions:
                new_positions[(virus_info[i][0], virus_info[i][1])] = []
            new_positions[(virus_info[i][0], virus_info[i][1])].append(virus_info[i])
 
        # 군집 합병 처리
        virus_info = []
        for key, group in new_positions.items():
            if len(group) > 1:
                total_count = sum(x[2] for x in group)
                max_count, max_dir = max(group, key=lambda x: x[2])[2:4]
                virus_info.append([key[0], key[1], total_count, max_dir])
            else:
                virus_info.append(group[0])
                 
    result = sum(count for _, _, count, _ in virus_info)
 
    print(f'#{test_case} {result}')