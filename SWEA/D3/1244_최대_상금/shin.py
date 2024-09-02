def dfs(a, depth):
    if change_num == depth:
        return int(''.join(a))
    max_num = 0
    for i in range(len(a)-1):
        for j in range(i + 1, len(a)):
            a[i], a[j] = a[j], a[i]
            visit = (tuple(a), depth + 1)
            if visit not in v:
                v.add(visit)
                max_num = max(max_num, dfs(a, depth + 1))
            a[i], a[j] = a[j], a[i]
    return max_num


T = int(input())
for tc in range(1, T + 1):
    num_string, change_num = input().split()
    num_string = list(num_string)
    change_num = int(change_num)
    v = set()

    result = dfs(num_string, 0)
    print(f"#{tc} {result}")
