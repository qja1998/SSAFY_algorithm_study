s = input()
stack = []
ans = 0
pre = ''
for c in s:
    if c == '(':
        stack.append(c)
    else:
        stack.pop()
        if pre == '(':
            ans += len(stack)
        else:
            ans += 1
    pre = c
print(ans)