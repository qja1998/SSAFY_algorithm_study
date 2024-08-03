import sys
input = sys.stdin.readline
n = int(input())
r, m = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

max_diff = 0
diff = 0
diff_sum = 0
pre_diff = -1

r *= 2

for j in range(2):
    for i in range(n - j):

        if i < n - 1:
            diff = pos[i + 1] - pos[i] - r
        else:
            diff = (pos[0] - pos[i]) % m - r

        if pre_diff > 0:
            if diff_sum == 0:
                diff_sum = pre_diff
            diff_sum += diff
            pre_diff = diff_sum
        else:
            diff_sum = 0
            pre_diff = diff

        max_diff = max(diff_sum, max_diff, diff)

result = (max_diff + 1) // 2

print(result)