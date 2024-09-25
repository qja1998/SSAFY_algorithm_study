T = int(input())
for test_case in range(1, T+1):
    price_list = list(map(int,input().split()))
    month_use_list = list(map(int, input().split()))
 
    pay_list = [0] * 13
 
    for i in range(1, 13):
        compare = [float("inf")] * 4
 
        compare[0] = pay_list[i-1] + (month_use_list[i-1] * price_list[0])
        compare[1] = pay_list[i-1] + price_list[1]
         
        if i > 2:
            compare[2] = pay_list[i-3] + price_list[2]
        if i == 12:
            compare[3] = price_list[3]
 
        pay_list[i] = min(compare)
 
    print(f"#{test_case} {pay_list[-1]}")