from collections import deque

test_case = int(input())

def rotate(gear_id, d):
    remain_gear = deque([(gear_id, d)])
    visited_gear = []
    while remain_gear:
        gear_id, d = remain_gear.popleft()
        gear = gears[gear_id]

        visited_gear.append(gear_id)

        # left gear
        if not (gear_id - 1 < 0 or gear_id - 1 in visited_gear):
            # check NS
            if not (gear[6] == gears[gear_id - 1][2]):
                remain_gear.append((gear_id - 1, -d))

        # right gear
        if not (gear_id + 1 >= 4 or gear_id + 1 in visited_gear):
            # check NS
            if not (gear[2] == gears[gear_id + 1][6]):
                remain_gear.append((gear_id + 1, -d))

        # gear rotate
        gears[gear_id].rotate(d)

def calculate_score():
    score = 0
    for i in range(4):
        score += gears[i][0] * 2 ** i

    return score

for t in range(test_case):
    k = int(input())

    gears = [deque(map(int, input().split())) for _ in range(4)]

    commands = [list(map(int, input().split())) for _ in range(k)]
    for gear_id, d in commands:
        rotate(gear_id - 1, d)
    
        # print(gears)
    score = calculate_score()

    print(f"#{t + 1} {score}")