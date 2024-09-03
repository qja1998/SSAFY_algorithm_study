TC = int(input())

for t in range(1, TC+1):
    n = int(input())

    nums = sorted(list(map(int, input().split())), reverse=True)

    result = [0] * 10
    even_i = 0
    odd_i = -1

    # 정렬된 수열을 앞 뒤로 반복하며 넣어줌
    for i in range(10):
        if i%2 == 0:
            result[i] = nums[even_i]
            even_i += 1
        else:
            result[i] = nums[odd_i]
            odd_i -= 1
    print(f"#{t} {' '.join(map(str, result))}")