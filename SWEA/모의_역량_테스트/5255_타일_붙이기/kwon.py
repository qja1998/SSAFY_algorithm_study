test_case = int(input())

memo = {}

def fill_tile(n, selected=[]):
    if n == 0:
        return 1
    
    if n in memo:
        return memo[n]
    
    cnt = 0
    if n >= 3:
        cnt += fill_tile(n-3, selected+[4])

    if n >= 2:
        cnt += fill_tile(n-2, selected+[2])
        cnt += fill_tile(n-2, selected+[3])
    
    if n >= 1:
        cnt += fill_tile(n-1, selected+[1])

    memo[n] = cnt

    return cnt
    

for t in range(test_case):
    n = int(input())

    print(f"#{t+1} {fill_tile(n)}")