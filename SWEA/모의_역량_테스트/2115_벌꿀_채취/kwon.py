test_case = int(input())

def make_subset(arr, depth, honey_num = 0, selected = []):
    if depth == -1:
        subsets.append(selected)
        return
    for i in range(2):
        if i == 0:
            make_subset(arr, depth - 1, honey_num, selected)
        else:
            if honey_num + arr[depth] > c:
                continue
            make_subset(arr, depth - 1, honey_num + arr[depth], selected + [arr[depth]])


def calcul_max_cost(subsets):
    max_cost = 0
    for subset in subsets:
        cost = 0
        for ele in subset:
            cost += ele ** 2

        max_cost = max(max_cost, cost)

    return max_cost

for t in range(test_case):
    n, m, c = map(int, input().split())
    honey_map = [list(map(int, input().split())) for _ in range(n)]
    total_max = 0

    for fst_i in range(n):
        for fst_j in range(n - m + 1):

            subsets = []
            make_subset(honey_map[fst_i][fst_j:fst_j + m], m - 1)
            fst_max = calcul_max_cost(subsets)

            for snd_i in range(n):
                start = 0
                if snd_i == fst_i:
                    start = fst_j + m
                for snd_j in range(start, n - m + 1):
                    subsets = []
                    make_subset(honey_map[snd_i][snd_j:snd_j + m], m - 1)
                    snd_max = calcul_max_cost(subsets)

                    total_max = max(total_max, fst_max + snd_max)

    print(f"#{t + 1} {total_max}")