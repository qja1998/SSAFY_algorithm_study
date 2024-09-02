for test_cast in range(10):
    T = int(input())
 
    password = list(map(int, input().split()))
    num_list = [1, 2, 3, 4, 5]
    num = 0
 
    while True:
        for i in range(len(num_list)):
            password.append(password[0] - num_list[i])
            password = password[1:len(password)]
            if password[len(password) - 1] <= 0:
                password[len(password)-1] = 0
                num = 1
                break
        if num == 1:
            break
 
    print('#'+str(T), *password)