test_case = int(input())

block_dict = {
    1: 1,
    2: 2,
    3: 2,
    4: 3
}

def fill_tile(n, selected=[]):
    if n == 0:
        return
    
    if n >= 3:
        fill_tile(n-3, selected+[4])

    if n >= 2:
        fill_tile(n-2, selected+[2])
        fill_tile(n-2, selected+[3])
    
    if n >= 1:
        fill_tile(n-1, selected+[1])

for t in range(test_case):
    n = int(input())

