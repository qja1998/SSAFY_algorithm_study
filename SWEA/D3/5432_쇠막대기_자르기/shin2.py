T = int(input())
for tc in range(1, T+1):
    case = input()
    result = 0
    stack = []
    for i in range((len(case))):
        if case[i] == ')':
            if case[i-1] == '(':
                stack.pop()
                result += len(stack)
            elif case[i-1] == ')':
                stack.pop()
                result += 1
        else:
            stack.append('(')
    print(f"#{tc} {result}")
