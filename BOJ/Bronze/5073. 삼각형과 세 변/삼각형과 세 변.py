while True:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    elif (a >= b + c) or (b >= a + c) or (c >= a + b):
        print("Invalid")
    elif a == b and b ==c:
        print("Equilateral")
    elif (a == b) or (b == c) or (c == a):
        print("Isosceles")
    elif a != b and b != c and a != c:
        print("Scalene")