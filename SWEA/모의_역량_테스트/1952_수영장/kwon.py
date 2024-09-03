test_case = int(input())

for t in range(1, test_case+1):
    prices = list(map(int, input().split()))
    plan_list = [0] + list(map(int, input().split()))

    dp = [0] * 13

    
    for i, (plan, dp_price) in enumerate(zip(plan_list[1:], dp), start=1):
        min_price = float('inf')
        
        min_price = min(min_price, plan_list[i-1] + prices[0]*plan)
        
        min_price = min(min_price, plan_list[i-1] + prices[1])

        if i >= 3:
            min_price = min(min_price, plan_list[i-3] + prices[2])

        plan_list[i] = min_price

    plan_list[-1] = min(plan_list[-1], prices[3])

    print(plan_list)
    print(f"#{t} {plan_list[-1]}")