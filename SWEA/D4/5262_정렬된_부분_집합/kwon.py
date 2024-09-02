from bisect import bisect_left

test_case = int(input())

for t in range(test_case):
    num_list = list(map(int, input().split()))

    result = []
    for num in num_list:
        idx = bisect_left(result, num)
        if idx == len(result):
            result.append(num)
        else:
            result[idx] = num

    print(f"#{t+1} {len(result)}")