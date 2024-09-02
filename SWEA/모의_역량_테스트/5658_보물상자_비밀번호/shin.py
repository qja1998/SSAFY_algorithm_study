from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num_count = N//4
    box = list(input())[::-1]
    turnning_box = [''.join(box[::-1])]
    result = set()
    queue = deque(box)
    for i in range(N):
        queue.append(queue.popleft())
        turnning_box.append(''.join(list(queue)[::-1]))
    for tb in turnning_box:
        for j in range(0, N, num_count):
            result.add(int(tb[j:j+num_count],16))
    result = sorted(list(result), reverse=True)
    print(f"#{tc} {result[K-1]}")
