result = []
def hanoi(n, p1, p2):
    if n == 1:
        result.append((p1, p2))
        return
    p3 = list(set([1, 2, 3]) - set([p1, p2]))[0]
    hanoi(n - 1, p1, p3)
    result.append((p1, p2))
    hanoi(n - 1, p3, p2)

n = int(input())
hanoi(n, 1, 3)

print(2 ** n - 1)
for i in result:
    print(i[0], i[1])