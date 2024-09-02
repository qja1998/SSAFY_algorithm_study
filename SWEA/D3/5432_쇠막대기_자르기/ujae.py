T = int(input())
 
for test_case in range(1, T+1):
    stick = list(input())
    stick_list = []
    stick_cut = 0
 
    for i in range(len(stick)):
        if stick[i] == '(':
            stick_list.append(stick[i])
        else:
            if stick[i-1] == '(':
                stick_list.pop()
                stick_cut += len(stick_list)
            else:
                stick_list.pop()
                stick_cut += 1
 
    print(f'#{test_case} {stick_cut}')