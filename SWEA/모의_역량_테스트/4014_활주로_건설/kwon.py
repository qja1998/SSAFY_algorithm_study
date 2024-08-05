test_case = int(input())

def chk_area(row, w):
    cnt = 1
    for i in range(n - 1):
        if row[i] == row[i + 1]:
            cnt += 1
        # 한 칸 위로
        elif row[i] + 1 == row[i + 1] and cnt >= w:
            cnt = 1
        # 한 칸 아래로
        elif row[i] - 1 == row[i + 1] and cnt >= 0:
            cnt = 1 - w
        # 두 칸 이상
        else:
            return False
    if cnt >= 0:
        return True
    return False

for t in range(test_case):
    n, w = map(int, input().split())
    terrain = [list(map(int, input().split())) for _ in range(n)]

    result = 0
    for row in terrain:
        if chk_area(row, w):
            result += 1

    for row in [[terrain[y][x] for y in range(n)] for x in range(n)]:
        if chk_area(row, w):
            result += 1

    print(f"#{t+1} {result}")