H, W = list(map(int, input().split()))

block_loc = list(map(int, input().split()))
result = 0
while True:
    max_list = []
    max_value = max(block_loc)
    for i in range(len(block_loc)):
        if max_value == block_loc[i]:
            max_list.append(i)
            block_loc[i] = block_loc[i] - 1
    if len(max_list) > 1:
        for j in range(len(max_list)-1):
            result += (max_list[j+1]-max_list[j]-1)
    if max_value == 0:
        print(result)
        break