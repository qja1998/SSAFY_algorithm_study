n = int(input())
a_i = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
for a in a_i:
    remain = a - b
    if remain > 0:
        if remain % c != 0:
            result += remain // c + 1
        else:
            result += remain // c
    result += 1

print(result)