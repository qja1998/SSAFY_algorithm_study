st = input().strip()+ '+'
total = 0
minus = False
num = ''
for c in st:
    if c.isdigit():
        num += c
    else:
        if minus:
            total -= int(num)
        else:
            total += int(num)
            
        if c == '-':
            minus = True

        num = ''
print(total)