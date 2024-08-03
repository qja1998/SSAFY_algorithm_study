n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))
    
memo = {}
def search(n: int, toggle: bool) -> int:
    if (n, toggle) in memo:
        return memo[(n, toggle)]
    if n < 0:
        return -1
    elif n == 0:
        return stair[0]
    elif n == 1:
        if toggle:
            return stair[0] + stair[1]
        else:
            return stair[1]
    elif toggle:
        pre = max(search(n-1, not toggle), search(n-2, toggle))
    else:
        pre = max(search(n-2, not toggle), search(n-3, toggle))
    memo[(n, toggle)] = pre + stair[n]
    return pre + stair[n]

print(search(n-1, True))