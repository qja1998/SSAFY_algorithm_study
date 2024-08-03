t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    order = list(range(n))
    cnt = 0
    while q:
        cur = q.pop(0)
        cur_order = order.pop(0)
        cnt += 1

        for i, num in enumerate(q):
            if num > cur:
                q.append(cur)
                tmp_q = q[:i]
                q = q[i:] + tmp_q
                order.append(cur_order)
                tmp_order = order[:i]
                order = order[i:] + tmp_order
                cur_order = -1
                cnt -= 1
                break
        if cur_order == m:
            break
    print(cnt)