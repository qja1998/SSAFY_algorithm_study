test_case = int(input())

for t in range(test_case):
    pipe_string = input().strip()

    stack = []
    pre_char = ''
    cnt = 0
    for char in pipe_string:
        if char == '(':
            stack.append(char)
        else:
            stack.pop()
            if pre_char == '(':
                cnt += len(stack)

            else:
                cnt += 1

        pre_char = char

    print(f'#{t+1} {cnt}')