test_case = int(input())

from collections import deque

CUSTOMER = ''

def chk_queue(chk):
    for ab, chk_time, customer in chk:
        if customer == '':
            return False
    return True


for t in range(test_case):
    n, m, k, a_target, b_target, = map(int, input().split())
    a_list = list(map(int, input().split()))
    a_chk = [[a, 0, CUSTOMER] for a in a_list]
    a_queue = deque()

    b_list = list(map(int, input().split()))
    b_chk = [[b, 0, CUSTOMER] for b in b_list]
    b_queue = deque()

    t_map = map(int, input().split())
    t_queue = deque((i, t) for i, t in enumerate(t_map, start=1))

    waiting_for_receipt_queue = deque([])
    waiting_for_repair_queue = deque([])
    time = 0

    a_visited = {i + 1: set([]) for i in range(n)}
    b_visited = {i + 1: set([]) for i in range(m)}

    while True:
        # 접수 창구
        # if t_queue: print(t_queue[0][1], time)
        while t_queue and t_queue[0][1] == time:
            waiting_for_receipt_queue.append(t_queue.popleft())
            a_queue.append(1)

        for i, (a, chk_time, customer) in enumerate(a_chk):
            # 고객 번호 낮은 순 / 창구 번호 낮은 순
            if customer == '' and waiting_for_receipt_queue:
                a_chk[i][1] = a
                a_chk[i][2] = waiting_for_receipt_queue.popleft()[0]
                a_visited[i + 1].add(a_chk[i][2])

            # 작업 진행
            a_chk[i][1] -= 1

        for i, (a, chk_time, customer) in enumerate(a_chk):
            # 접수 처리가 끝난 고객 수리 대기열로
            # 먼저 기다리는 순
            # 동시에 왔을 경우 접수 창구 번호 낮은 순
            if chk_time == 0 and customer != '':
                waiting_for_repair_queue.append(customer)
                a_chk[i][1] = a
                a_chk[i][2] = ''
                a_queue.popleft()
                b_queue.append(1)

        # 정비 창구
        for i, (b, chk_time, customer) in enumerate(b_chk):
            # 여러 곳 비었을 경우, 정비 창구 번호 작은 순
            if customer == '' and waiting_for_repair_queue:
                b_chk[i][1] = b
                b_chk[i][2] = waiting_for_repair_queue.popleft()
                b_visited[i + 1].add(b_chk[i][2])

            # 작업 진행
            b_chk[i][1] -= 1

        for i, (b, chk_time, customer) in enumerate(b_chk):
            if chk_time == 0 and customer != '':
                b_chk[i][1] = b
                b_chk[i][2] = ''
                b_queue.popleft()

        if b_queue or a_queue or t_queue:
            time += 1
            continue
        break

    # print(a_visited, b_visited)
    # print(a_visited[a_target].intersection(b_visited[b_target]))
    result = sum(a_visited[a_target].intersection(b_visited[b_target]))
    print(f"#{t+1} {result if result else -1}")
