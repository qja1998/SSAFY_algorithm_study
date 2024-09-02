T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    op_input_list = list(map(int, input().split()))
    number_list = list(map(int, input().split()))

    max_num = -100000000
    min_num = 100000000

    def create_num(op_list, idx, res):
        global max_num, min_num

        if idx == N:
            max_num = max(max_num, res)
            min_num = min(min_num, res)
            return
        
        for op_idx, op_cnt in enumerate(op_list):
            if op_cnt == 0:
                continue
            tmp_res = res
            if op_idx == 0:
                tmp_res += number_list[idx]
            elif op_idx == 1:
                tmp_res -= number_list[idx]
            elif op_idx == 2:
                tmp_res *= number_list[idx]
            elif op_idx == 3:
                if number_list[idx] == 0:
                    return
                tmp_res = int(tmp_res / number_list[idx])
            else:
                print("주어진 입력이 아닙니다 ~~~~ ")

            op_list[op_idx] -= 1
            create_num(op_list, idx + 1, tmp_res)
            op_list[op_idx] += 1

    init_num = number_list[0]
    init_idx = 1

    create_num(op_input_list, init_idx, init_num)
    print(f"#{test_case} {max_num - min_num}")
