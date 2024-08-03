n = int(input())

meetings = [0] * n
for i in range(n):
    meetings[i] = list(map(int, input().split()))

max_p = 0

def com_p(day, p=0, meetings=meetings, n=n):
    global max_p
    
    if day >= n:
        max_p = max(max_p, p)
        return

    cur_t, cur_p = meetings[day]

    for d in range(0, n - day):
        next_day = day + cur_t + d
        if next_day <= n:
            com_p(next_day, p + cur_p)
        else:
            com_p(next_day, p)

for day in range(n):
    com_p(day)

print(max_p)