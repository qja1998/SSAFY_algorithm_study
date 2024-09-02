dict = {1:(-1, 0), 2:(1, 0), 3:(0, -1), 4:(0, 1)}


def new_microbe_info(mic_info):
    sum_mic = {}
    max_dir = {}

    for item in mic_info:
        coord = (item[0], item[1])
        if item[2] == 0:
            continue
        else:
            value = item[2]
        direction = item[3]

        if coord in sum_mic:
            sum_mic[coord] += value
        else:
            sum_mic[coord] = value

        if coord not in max_dir or value > max_dir[coord][0]:
            max_dir[coord] = (value, direction)

    result = []
    for coord in sum_mic:
        total_sum = sum_mic[coord]
        pre_dir = max_dir[coord][1]
        result.append([coord[0], coord[1], total_sum, pre_dir])

    return result


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    microbe = [list(map(int,input().split())) for _ in range(K)]
    prohibit_area = [(i,j) for i in range(N) for j in range(N) if (i == 0 or i == N-1) or (j == 0 or j == N-1)]
    mic_count = 0

    for i in range(M):
        for mic in microbe:
            mic_index = microbe.index(mic)
            mic[0] += dict[mic[3]][0]
            mic[1] += dict[mic[3]][1]
            if (mic[0], mic[1]) in prohibit_area:
                mic[2] //= 2
                if mic[3] == 1:
                    mic[3] = 2
                elif mic[3] == 2:
                    mic[3] = 1
                elif mic[3] == 3:
                    mic[3] = 4
                elif mic[3] == 4:
                    mic[3] = 3
        microbe = new_microbe_info(microbe)

    for mic in microbe:
        mic_count += mic[2]
    print(f"#{tc} {mic_count}")