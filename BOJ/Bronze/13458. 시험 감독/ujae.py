N = int(input())

person = list(map(int, input().split()))
B, C = map(int, input().split())

person = list(map(lambda x: x-B, person))
result = N

for i in range(len(person)):
    if person[i] > 0:
        if person[i] % C == 0:
            result += int(person[i]/C)
        else:
            result += int(person[i]/C) + 1

print(result)