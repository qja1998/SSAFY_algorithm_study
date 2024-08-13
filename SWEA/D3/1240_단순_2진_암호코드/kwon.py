test_case = int(input())

code_dict = {
    (0, 0, 0, 1, 1, 0, 1) : 0,
    (0, 0, 1, 1, 0, 0, 1) : 1,
    (0, 0, 1, 0, 0, 1, 1) : 2,
    (0, 1, 1, 1, 1, 0, 1) : 3,
    (0, 1, 0, 0, 0, 1, 1) : 4,
    (0, 1, 1, 0, 0, 0, 1) : 5,
    (0, 1, 0, 1, 1, 1, 1) : 6,
    (0, 1, 1, 1, 0, 1, 1) : 7,
    (0, 1, 1, 0, 1, 1, 1) : 8,
    (0, 0, 0, 1, 0, 1, 1) : 9
}


for t in range(test_case):
    find_chk = False
    n, m = map(int, input().split())
    for i in range(n):
        row = [int(num) for num in input()]

        if sum(row) != 0 and not find_chk:
            for i in range(m-1, -1, -1):
                num = row[i]
                if num == 1:
                    start_x = i
                    find_chk = True
                    break
            code_row = row[start_x - 55: start_x + 1]

    nums_decoded = []
    for i in range(0, 56, 7):
        nums_decoded.append(code_dict[tuple(code_row[i:i+7])])
    chk = sum(nums_decoded[::2]) * 3 + sum(nums_decoded[1::2])
    if chk % 10 == 0:
        print(sum(nums_decoded))
    else:
        print(0)