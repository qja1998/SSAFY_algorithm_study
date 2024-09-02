T = int(input())
 
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    password = input()
 
    passwords = set()
    num_count = N//4
 
    for _ in range(len(password)):
        for j in range(0, N, num_count):
            passwords.add(password[j:j+num_count])
        password = password[-1] + password[0:-1]
 
    passwords_list = [int(num, 16) for num in list(passwords)]
    passwords_list.sort(reverse=True)
    print(f'#{test_case} {passwords_list[K-1]}')
