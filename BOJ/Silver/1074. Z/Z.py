import sys
N, y, x = map(int, sys.stdin.readline().split())

def position(N, x, y, base=0):
    if N == 0 or (x <= 1 and y <= 1):
        print(base)
        return base
    
    num = 2 ** (N - 1)
    if x <= num and y <= num:
        position(N-1, x, y, base)
        
    elif x > num and y <= num:
        position(N-1, x - num, y, 4 ** (N - 1) + base)
    
    elif x <= num and y > num:
        position(N-1, x, y - num, 2 * 4 ** (N - 1) + base)
        
    elif x > num and y > num:
        position(N-1, x - num, y - num, 3 * 4 ** (N - 1) + base)
        
position(N, x + 1, y + 1)