a, b, c = map(int, input().split())
if (a==b and a != c) or(a==c and a != b):
    print(1000+a*100)
elif (b==c and b != a):
    print(1000+b*100)
elif (a==b==c):
    print(10000+a*1000)
else:
    max = 0
    for i in [a, b, c]:
        if i > max:
            max = i
    print(max*100)