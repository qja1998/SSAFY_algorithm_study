test_case = int(input())

# 해당 arr의 모든 subset을 만들어 반환
def make_subset(arr, depth, honey_num = 0, selected = []):
    if depth == -1:
        subsets.append(selected)
        return
    for i in range(2):
        if i == 0: # 현재 depth 넣지 않는 경우
            make_subset(arr, depth - 1, honey_num, selected)
        else: # 현재 depth 넣는 경우
            # 만약 c를 넘으면 진행하지 않음
            if honey_num + arr[depth] > c:
                continue
            make_subset(arr, depth - 1, honey_num + arr[depth], selected + [arr[depth]])


# 주어진 수들로 실제 금액을 계산
def calcul_max_cost(subsets):
    max_cost = 0
    for subset in subsets:
        cost = 0
        for ele in subset:
            cost += ele ** 2

        # 최대 금액을 바로 갱신
        max_cost = max(max_cost, cost)

    return max_cost

for t in range(test_case):
    n, m, c = map(int, input().split())
    honey_map = [list(map(int, input().split())) for _ in range(n)]
    total_max = 0

    # 두 인부가 고르게 하고 subset을 만들어 계산
    # 첫 번째 인부가 꿀통 고름
    for fst_i in range(n):
        for fst_j in range(n - m + 1):

            subsets = []
            make_subset(honey_map[fst_i][fst_j:fst_j + m], m - 1)
            fst_max = calcul_max_cost(subsets)

            # 두 번째 인부가 꿀통 고름
            for snd_i in range(n):
                start = 0
                # i가 같으면 m칸 뒤로 미루기
                if snd_i == fst_i:
                    start = fst_j + m
                # 고르지 않은 꿀통 고르기
                for snd_j in range(start, n - m + 1):
                    subsets = []
                    make_subset(honey_map[snd_i][snd_j:snd_j + m], m - 1)
                    snd_max = calcul_max_cost(subsets)

                    total_max = max(total_max, fst_max + snd_max)

    print(f"#{t + 1} {total_max}")