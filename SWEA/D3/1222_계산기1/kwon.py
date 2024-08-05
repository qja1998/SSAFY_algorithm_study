for i in range(10):
    n = int(input())
    order_string = input()

    postfix = ''
    operator = ''

    for char in order_string:
        if char.isalnum():
            postfix += char
        else:
            operator += char

    postfix += operator

    stack = []
    result = 0
    for char in postfix:
        if char.isalnum():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = 0
            if char == '+':
                result = operand1 + operand2
            stack.append(result)

    print(f"#{i + 1} {result}")
