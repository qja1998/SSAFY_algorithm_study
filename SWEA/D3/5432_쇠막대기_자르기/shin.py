T = int(input())
for tc in range(1, T+1):
    case = input().replace("()","L")
    stick, laser, total = 0, 0, 0
    for i in case:
        if i == "(": stick += 1; total += 1
        if i == ")": stick -= 1
        if i == "L": laser += stick
    print(f"#{tc} {total + laser}")
