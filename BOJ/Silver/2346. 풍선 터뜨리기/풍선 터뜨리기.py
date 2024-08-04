n = int(input())
balloons = list(map(int, input().split()))
balloons = [(i + 1, b) for i, b in enumerate(balloons)]
num = 0
while balloons:
    print(balloons[num][0], end=' ')
    i, paper = balloons[num]
    n -= 1
    if n != 0:
        if paper > 0:
            num = (num + paper - 1) % n
        else:
            num = (num + paper) % n
    else:
        num = 0
    balloons.remove((i, paper))