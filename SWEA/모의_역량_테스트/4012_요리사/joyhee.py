def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i + 1:], n - 1):
            result.append([elem] + rest)
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    food_list = comb([i for i in range(N)], N/2)
    syn_list1 = []
    syn_list2 = []
    temp = []
    for j in range(len(food_list)):
        syn_list1.append(comb([i for i in food_list[j]], 2))
        for z in range(N):
            if z in food_list[j]:
                continue
            temp.append(z)
        syn_list2.append(comb(temp, 2))
        temp = []

    point1 = []
    point2 = []
    syn_score = 0
    for num_of_c in syn_list1:
        for i, j in num_of_c:
            syn_score = syn_score + synergy[i][j] + synergy[j][i]
        point1.append(syn_score)
        syn_score = 0
    for num_of_c in syn_list2:
        for i, j in num_of_c:
            syn_score = syn_score + synergy[i][j] + synergy[j][i]
        point2.append(syn_score)
        syn_score = 0

    diff = []
    for i in range(len(point1)):
        diff.append(abs(point1[i]-point2[i]))
    print(f"#{tc} {min(diff)}")