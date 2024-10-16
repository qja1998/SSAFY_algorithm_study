import heapq

N, H, T = list(map(int, input().split()))

heights = [int(input()) for _ in range(N)]

max_heap = []

for height in heights:
    heapq.heappush(max_heap, (-height, height))

for i in range(T+1):
    max_val = heapq.heappop(max_heap)[1]
    if max_val != 0 and max_val < H:
        print("YES")
        print(i)
        exit()
    else:
        if i == T:
            heapq.heappush(max_heap, (-max_val, max_val))
            break
        max_val = int(max_val/2)
        heapq.heappush(max_heap, (-max_val, max_val))

print("NO")
result = heapq.heappop(max_heap)[1]
if result == 0:
    print(1)
else:
    print(result)
