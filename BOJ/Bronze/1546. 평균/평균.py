n = int(input())
scores = list(map(int, input().split()))

best = max(scores)
new = 0

for score in scores:
    new += score / best * 100

print(new / n)