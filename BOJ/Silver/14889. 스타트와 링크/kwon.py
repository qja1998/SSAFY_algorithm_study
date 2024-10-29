from itertools import combinations
N = int(input())

member_mat = [list(map(int, input().split())) for _ in range(N)]

# 대각선 합 미리 모두 계산
stat_sum = [sum(mem1) + sum(mem2) for mem1, mem2 in zip(member_mat, zip(*member_mat))]
stat_total = sum(stat_sum) // 2
result = float('inf')

# 팀 조합
for l in combinations(stat_sum, N//2):
    result = min(result, abs(stat_total - sum(l)))
print(result)