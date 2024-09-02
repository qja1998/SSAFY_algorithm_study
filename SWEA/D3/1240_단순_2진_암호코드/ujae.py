T = int(input())
 
pass_dict = {'0001101' : 0, '0011001' : 1, '0010011': 2, '0111101': 3, '0100011': 4
             , '0110001' : 5, '0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}
 
for test_cast in range(1, T+1):
    n, m = map(int, input().split())
    num=0
 
    for _ in range(n):
        password = input()
        if '1' in password:
            idx = password.rfind('1')
            password = (password[idx-55:idx+1])
            pass_dan = []
            for i in range(len(password)//7):
                pass_dan.append(pass_dict[str(password[i*7:7+(7*i)])])
 
            if num==1:
                continue
 
            if ((sum(pass_dan[0::2])*3)+sum(pass_dan[1::2])) % 10 == 0:
                print(f'#{test_cast} {sum(pass_dan[:])}')
                num=1
    if num==0:
        print(f'#{test_cast} {0}')