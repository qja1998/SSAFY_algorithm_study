import copy
 
for test_case in range(10):
    T=int(input())
    ladder=[]
    result=0
    for i in range(100):
        ladder_list = list(map(int,input().split()))
        ladder.append(ladder_list)
    for x in range(100):
        loc = copy.deepcopy(x)
        y=0
        if ladder[0][x] == 1:
            while y < 99:
                if x<0 and x<99:
                    if ladder[y][x-1] == 0 and ladder[y][x+1] == 0:
                        y += 1
                else:
                    if x > 0 and ladder[y][x-1] == 1:
                        while x>0 and ladder[y][x-1] == 1:
                            x -= 1
                        y+=1
                    else:
                        while x<99 and ladder[y][x+1] == 1:
                            x += 1
                        y+=1
 
        if ladder[y][x] == 2:
            result=loc
    print(f"#{T} {result}")