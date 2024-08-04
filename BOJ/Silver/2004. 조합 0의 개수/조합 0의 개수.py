n, m = map(int, input().split())

def com_ten(n, m):
    cnt_two_n, cnt_five_n = 0, 0
    cnt_two_m, cnt_five_m, cnt_two_nm, cnt_five_nm = 0, 0, 0, 0
    two, five = 2, 5
    nm = n - m

    while n >= two:
        if m >= two:
            cnt_two_m += m // two
        if nm >= two:
            cnt_two_nm += nm // two
        cnt_two_n += n // two
        two *= 2

    while n >= five:
        if m >= five:
            cnt_five_m += m // five
        if nm >= five:
            cnt_five_nm += nm // five
        cnt_five_n += n // five
        five *= 5
            
    return cnt_two_n, cnt_five_n, cnt_two_m, cnt_five_m, cnt_two_nm, cnt_five_nm

cnt_two_n, cnt_five_n, cnt_two_m, cnt_five_m, cnt_two_nm, cnt_five_nm = com_ten(n, m)
t = cnt_two_n - cnt_two_m - cnt_two_nm
f = cnt_five_n - cnt_five_m - cnt_five_nm

print(min(t, f))

