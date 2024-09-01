from collections import defaultdict
TC = int(input())

def init_dict():
    return [1]

for t in range(1, TC+1):
    n, a, b = map(int, input().split())
    a -= 1

    memo_dict = defaultdict(init_dict)
    memo_dict[0] = [1]
    memo_dict[1] = [1, 1]

    for i in range(2, n+1):
        for j in range(1, i):
            memo_dict[n].append(memo_dict[n-1][j] + memo_dict[n-1][j-1])
        memo_dict[n].append(1)

    print(f"#{t} {memo_dict[n][a]}")