from collections import deque, defaultdict


def find_computer():
    queue = deque([1])
    while queue:
        number = queue.popleft()
        if number not in result:
            for i in computer_dict[number]:
                queue.append(i)
            result.add(number)


N = int(input())
M = int(input())
computer_info = [list(map(int, input().split())) for _ in range(M)]

computer_dict = defaultdict(list)

for num1, num2 in computer_info:
    computer_dict[num1].append(num2)
    computer_dict[num2].append(num1)

result = set()
find_computer()
print(len(result)-1)
