n = int(input())

room = 1
num = 1

while n > room:
    room += num * 6
    num += 1

print(num)