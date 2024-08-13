# 계산

def calculate(num1, num2, operator):

    if operator == '+':
        num1 += num2
    elif operator == '-':
        num1 -= num2
    elif operator == '*':
        num1 *= num2
    elif operator == '/':
        num1 = int(num1 / num2)
    return num1

# 수식 완성
def search_expression(i, result):
    if i == n:
        global max_num, min_num
        max_num = max(max_num, result)
        min_num = min(min_num, result)
        return

    for operator in operators:
        if operator_dict[operator] > 0:
            operator_dict[operator] -= 1
            search_expression(i + 1, calculate(result, nums[i+1], operator))
            operator_dict[operator] += 1



test_case = int(input())

for t in range(test_case):
    n = int(input()) - 1
    operators = ['+', '-', '*', '/']
    operator_dict = {operator: cnt for operator, cnt in zip(operators, map(int, input().split()))}

    nums = list(map(int, input().split()))

    max_num = float('-inf')
    min_num = float('inf')
    result_dict = {}
    visited = []

    search_expression(0, nums[0])

    print(f"#{t + 1} {max_num - min_num}")