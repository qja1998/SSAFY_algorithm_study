n = int(input())
nums = sorted(list(map(int, input().split())))

i = 0
result = 0
ans = []

while nums:
    if n % 2 and i == n - 1:
        tmp = nums.pop()
        if abs(tmp - ans[0]) < abs(tmp - ans[-1]):
            ans.append(tmp)
        else:
            ans.insert(0, tmp)
    elif i % 4 == 0:
        ans.insert(0, nums.pop(0))
    elif i % 4 == 1:
        ans.append(nums.pop(-1))
    elif i % 4 == 2:
        ans.insert(0, nums.pop(-1))
    elif i % 4 == 3:
        ans.append(nums.pop(0))
    i += 1

for i in range(n-1):
    result += abs(ans[i] - ans[i + 1])

print(result)