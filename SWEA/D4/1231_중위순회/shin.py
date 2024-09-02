def in_order(node):
    if node:
        in_order(data[node][2])
        print(data[node][1], end='')
        in_order(data[node][3])

for tc in range(1, 11):
    N = int(input())

    data = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split())) for _ in range(N)]

    for arr in data:
        while len(arr) != 4:
            arr.append(0)

    data.insert(0,[0,0,0,0])

    print(f"#{tc}", end=' ')
    in_order(1)
    print()
