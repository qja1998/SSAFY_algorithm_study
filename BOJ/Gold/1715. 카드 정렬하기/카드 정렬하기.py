import heapq

n = int(input())
numbers = [int(input()) for _ in range(n)]

heapq.heapify(numbers)

result = 0

while len(numbers) > 1:
    x = heapq.heappop(numbers)
    y = heapq.heappop(numbers)
    result += x + y
    heapq.heappush(numbers, x + y)

print(result)