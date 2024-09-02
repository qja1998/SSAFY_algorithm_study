def search_leader(x, y):
    ladder_arr[x][y] = 0

    if x == 0:
        return y

    if y > 0 and ladder_arr[x][y - 1] == 1:
        left = search_leader(x, y - 1)
        if left is not None:
            return left

    if y < 99 and ladder_arr[x][y + 1] == 1:
        right = search_leader(x, y + 1)
        if right is not None:
            return right

    if x > 0 and ladder_arr[x - 1][y] == 1:
        up = search_leader(x - 1, y)
        if up is not None:
            return up

    return None

for _ in range(1, 11):
    T = int(input())
    ladder_arr = [list(map(int, input().split())) for i in range(100)]
    # arrive_coordinates = [98]+[i for i in range(100) if ladder_arr[99][i] == 2]
    # print(f"#{T} {search_leader(arrive_coordinates[0],arrive_coordinates[1])}")
    arrive_coordinates = [i for i in range(100) if ladder_arr[99][i] == 2]
    print(f"#{T} {search_leader(98, arrive_coordinates[0])}")