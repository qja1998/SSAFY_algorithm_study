# 가장 큰 거인부터 때리기
# 모두 다 작게 할 수 있나
import sys
import heapq

input = sys.stdin.readline

N, H, T = map(int, input().split())

giant = [-int(input()) for _ in range(N)]

heapq.heapify(giant)

cnt = 0
for t in range(T):
    g = -heapq.heappop(giant)
    if g < H:
        break
    if g != 1:
        g //= 2
        cnt += 1
    heapq.heappush(giant, -g)

available = True
max_g = 0
for g in giant:
    g = -g
    if g >= H:
        available = False
    max_g = max(max_g, g)

print('YES' if available else 'NO')
print(cnt if available else max_g)