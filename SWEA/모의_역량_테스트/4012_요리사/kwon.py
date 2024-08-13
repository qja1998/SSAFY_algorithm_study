test_case = int(input())

def search_recipe(index_list, n):
    if n == 1 :
        return [[i] for i in index_list]
    result = []
    for i in range(len(index_list) - 1):
        for j in search_recipe(index_list[i+1:], n - 1):
            result.append([index_list[i]] + j)
    
    return result



for t in range(test_case):
    n = int(input())
    min_diff = float('inf')

    recipe = [list(map(int, input().split())) for _ in range(n)]

    # for i in range(n):
    #     for j in range(i + 1, n):
    #         recipe[i][j] += recipe[j][i]
    #         recipe[j][i] = recipe[i][j]
    
    index_set = set(range(n))

    comb_list = [[0] + c for c in search_recipe(list(range(1, n)), n // 2 - 1)]

    for comb in comb_list:
        comb2 = list(index_set - set(comb))
        food1, food2 = 0, 0

        for i_idx, (i1, i2) in enumerate(zip(comb, comb2)):
            for j1, j2 in zip(comb[i_idx + 1:], comb2[i_idx + 1:]):
                food1 += recipe[i1][j1] + recipe[j1][i1]
                food2 += recipe[i2][j2] + recipe[j2][i2]
        min_diff = min(min_diff, abs(food1 - food2))



    print(f"#{t + 1} {min_diff}")