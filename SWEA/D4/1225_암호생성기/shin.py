from collections import deque

for _ in range(10):
    tc = int(input())
    num_for_pw_list = list(map(int,input().split()))
    pw_queue = deque(num_for_pw_list)

    cycle_num = 1
    while True:
        if cycle_num > 5:
            cycle_num = 1
        pop_num = pw_queue.popleft() - cycle_num
        if pop_num <= 0:
            pw_queue.append(0)
            break
        pw_queue.append(pop_num)
        cycle_num += 1

    print(f"#{tc}", *pw_queue)
