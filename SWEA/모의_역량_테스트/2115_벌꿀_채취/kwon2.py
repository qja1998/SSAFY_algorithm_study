# test_case = int(input())


def max_subset_sum(arr):
    dp = [[0, 0]] * (c + 1)

    for num in arr:
        for j in range(c, num - 1, -1):
            next_sq_value = dp[j - num][1] + num ** 2
            if dp[j - num][0] + num > c:
                continue
            if next_sq_value > dp[j - num][1]:
                dp[j][0] = dp[j - num][0] + num
                dp[j][1] = next_sq_value
    _, max_sum = max(dp, key=lambda x: x[1])
    print(dp)
    return max_sum


# for t in range(test_case):
#     n, m, c = map(int, input().split())

#     honey_map = [list(map(int, input().split())) for _ in range(n)]
#     max_honey_benefit = 0

#     for y1 in range(n):
#         for x1 in range(y1, n - m):
#             honey_area1 = honey_map[y1][x1 : x1+m]
#             max_sum1 = max_subset_sum(honey_area1)

#             for y2 in range(n):
#                 start = 0
#                 if y1 == y2:
#                     start = x1 + m
#                 for x2 in range(start, n - m):
#                     honey_area2 = honey_map[y2][x2 : x2+m]
#                     max_sum2 = max_subset_sum(honey_area2)

#                     max_honey_benefit = max(max_honey_benefit, max_sum1 + max_sum2)
    
#     print(f"#{t+1} {max_honey_benefit}")


arr = [1, 2, 3, 4]
c = 9

print(max_subset_sum(arr))