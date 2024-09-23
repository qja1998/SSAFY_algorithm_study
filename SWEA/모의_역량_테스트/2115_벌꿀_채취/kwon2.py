# DP


def max_subset_sum(arr):
    # 제한(c)을 길이로하는 DP 배열
    dp = [[0, 0] for _ in range(c + 1)]


    for num in arr:
        for j in range(c, num - 1, -1):
            # 제한을 넘어가면 스킵
            if dp[j - num][0] + num > c:
                continue
            next_sq_value = dp[j - num][1] + num ** 2
            # 지금 계산한 점수가 저장된 점수보다 크면 갱신
            if next_sq_value > dp[j][1]:
                dp[j][0] = dp[j - num][0] + num
                dp[j][1] = next_sq_value
    # 최대값 추출
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
                    # 추출한 최대값으로 전체 최대값을 갱신
                    total_max = max(total_max, fst_max + snd_max)

    print(f"#{t + 1} {total_max}")