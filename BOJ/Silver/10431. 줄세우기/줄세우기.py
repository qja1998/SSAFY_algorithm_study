n = int(input())

for _ in range(n):
    case = list(map(int, input().split()))
    t = case[0]
    case = case[1:]

    counter = {}
    for c in case:
        for num in counter:
            if num > c:
                counter[num] += 1
        counter[c] = 0

    print(t, sum(counter.values()))