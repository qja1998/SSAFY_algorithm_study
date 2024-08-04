n = int(input())

neg_cnt = [0] * 1001
pos_cnt = [0] * 1001
zero = False

pos_max = 0
neg_min = 0

for _ in range(n):
    num = int(input())
    if num > 0:
        pos_cnt[num] += 1
        if num > pos_max:
            pos_max = num
    elif num < 0:
        neg_cnt[num] += 1
        if num < neg_min:
            neg_min = num
    else:
        zero = True

remain_num = 0
result = 0

# positive numbers
for num in range(pos_max, 1, -1):
    num_cnt = pos_cnt[num]
    if num_cnt == 0:
        continue

    if remain_num:
        result += num * remain_num
        num_cnt -= 1

    result += num_cnt // 2 * num ** 2

    if num_cnt % 2:
        remain_num = num
    else:
        remain_num = 0

result += remain_num
result += pos_cnt[1]
remain_num = 0


# negative numbers
for num in range(neg_min, 0):
    num_cnt = neg_cnt[num]
    if num_cnt == 0:
        continue

    if remain_num:
        result += num * remain_num
        num_cnt -= 1

    result += num_cnt // 2 * num ** 2

    if num_cnt % 2:
        remain_num = num
    else:
        remain_num = 0


if not zero:
    result += remain_num

print(result)