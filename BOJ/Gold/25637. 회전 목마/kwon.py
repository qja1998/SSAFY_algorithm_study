N = int(input())

people = list(map(int, input().split()))

left_zero = 0
right_zero = 0
for i in range(N):
    if people[i]