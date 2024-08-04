t = int(input())

def cnt_bracket(string):
    cnt_list = [0] * 1500000
    cnt = -1
    tmp = 0
    for i, c in enumerate(string):
        if c == '(':
            cnt += 1
            if string[i + 1] == ')':
                cnt_list[cnt] += 1
                tmp = max(tmp, cnt)
        else:
            cnt -= 1
    for i in range(1500000 - 1):
        cnt_list[i + 1] += cnt_list[i] // 2
        cnt_list[i] %= 2
        
    return cnt_list, tmp + 1

for _ in range(t):
    a = input()
    b = input()

    cnt_a, max_a = cnt_bracket(a)
    cnt_b, max_b = cnt_bracket(b)

    max_val = max(max_a, max_b)


    ans = '='
    for i in range(1500000 - 1, -1, -1):
        tmp_a, tmp_b = cnt_a[i], cnt_b[i]
        if tmp_a > tmp_b:
            ans = '>'
            break
        elif tmp_a < tmp_b:
            ans = '<'
            break
    print(ans)