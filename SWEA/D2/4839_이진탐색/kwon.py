TC = int(input())

def bisect(l, r, c, target, n=0):
    if c == target:
        return n
    if c < target:
        l = c
    else:
        r = c
    return bisect(l, r, int((l+r)/2), target, n+1)


for t in range(1, TC+1):
    P, A, B = map(int, input().split())

    a_cnt = bisect(0, P, int(P/2), A)
    b_cnt = bisect(0, P, int(P/2), B)

    if a_cnt == b_cnt:
        print(f"#{t} 0")
    elif a_cnt < b_cnt:
        print(f"#{t} A")
    elif a_cnt > b_cnt:
        print(f"#{t} B")