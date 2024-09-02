for test_cast in range(10):
    n = int(input())
    num_list = input()
    cal = ""
    cal_temp = ""
    result = []
    for i in range(len(num_list)):
        if num_list[i] != '+':
            cal += (num_list[i])
        else:
            if len(cal) == 1:
                cal_temp += (num_list[i])
                continue
            else:
                cal += (num_list[i])
    cal += cal_temp
 
    for j in range(len(cal)):
        if cal[j] != '+':
            result.append(cal[j])
        else:
            a = int(result.pop())
            b = int(result.pop())
            result.append(a+b)
 
    print('#'+str(test_cast+1), *result)