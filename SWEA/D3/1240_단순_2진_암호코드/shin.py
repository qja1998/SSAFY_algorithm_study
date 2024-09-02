dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    password_code = [input() for _ in range(N)]
    password_string = ''

    for pc in password_code:
        if '1' in pc:
            ps = pc.strip('0')
            password_string = '0'*(56 - len(ps)) + ps
            break

    seven_parsing = [password_string[i:i+7] for i in range(0, len(password_string), 7)]

    result_list = [dict[part] for part in seven_parsing]

    odd_num = 0
    cal_num = 0
    for i in range(8):
        if i % 2 == 0: # 실제론 이게 홀수 자리
            odd_num += result_list[i]
        else:
            cal_num += result_list[i]
    cal_num += (odd_num * 3)

    if cal_num % 10 == 0:
        answer = sum(result_list)
    else:
        answer = 0

    print(f"#{tc} {answer}")
