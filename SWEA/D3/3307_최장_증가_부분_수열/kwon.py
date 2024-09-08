import bisect

TC = int(input())

for t in range(1, TC+1):
    n = int(input())
    nums = list(map(int, input().split()))

    result_list = []

    for num in nums:
        idx = bisect.bisect_left(result_list, num)
        if idx == len(result_list):
            result_list.append(num)
        else:
            result_list[idx] = num
    
    print(f"#{t} {len(result_list)}")