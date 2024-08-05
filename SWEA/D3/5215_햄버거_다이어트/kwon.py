
# DP 풀이
test_case = int(input())

for t in range(test_case):
    n, l = map(int, input().split())

    hamburgers = [list(map(int, input().split())) for _ in range(n)]

    dp = [0] * (l + 1)

    for score, cal in hamburgers:
        for j in range(l, cal - 1, -1):
            dp[j] = max(dp[j], dp[j - cal] + score)

    max_score = max(dp)

    print(f"#{t + 1} {max_score}")


# DFS 풀이
test_case = int(input())

# 제한 칼로리 내에서 최대의 맛
def search_best(hamburgers, sum_cal=0, sum_score=0):
    global max_score
    max_score = max(max_score, sum_score)

    for i, (score, cal) in enumerate(hamburgers):
        if sum_cal + cal > l:
            continue
        search_best(hamburgers[i + 1:], sum_cal + cal, sum_score + score)


for t in range(test_case):
    n, l = map(int, input().split())

    hamburgers = [list(map(int, input().split())) for _ in range(n)]

    max_score = 0

    search_best(hamburgers)

    print(f"#{t + 1} {max_score}")