import heapq
test_case = int(input())

for t in range(test_case):
    n = int(input())
    tmp = f"#{t + 1} "
    heap = []
    heapq.heapify(heap)
    for _ in range(n):
        cmd = input()
        if len(cmd) == 1:
            if heap:
                tmp += str(-heapq.heappop(heap)) + ' '
            else:
                tmp += '-1 '
        else:
            cmd, num = map(int, cmd.split())
            heapq.heappush(heap, -num)
    print(tmp)