def max_subset_sum(arr):
    dp = [[0, 0] for _ in range(c + 1)]

    for num in arr:
        for j in range(c, num - 1, -1):
            if dp[j - num][0] + num > c:
                continue
            next_sq_value = dp[j - num][1] + num ** 2
            if next_sq_value > dp[j][1]:
                dp[j][0] = dp[j - num][0] + num
                dp[j][1] = next_sq_value
    _, max_sum = max(dp, key=lambda x: x[1])
    return max_sum

test_case = int(input())

for t in range(test_case):
    n, m, c = map(int, input().split())
    honey_map = [list(map(int, input().split())) for _ in range(n)]
    total_max = 0

    for fst_i in range(n):
        for fst_j in range(n - m + 1):

            fst_max = max_subset_sum(honey_map[fst_i][fst_j:fst_j + m])

            for snd_i in range(n):
                start = 0
                if snd_i == fst_i:
                    start = fst_j + m
                for snd_j in range(start, n - m + 1):
                    snd_max = max_subset_sum(honey_map[snd_i][snd_j:snd_j + m])

                    total_max = max(total_max, fst_max + snd_max)

    print(f"#{t + 1} {total_max}")