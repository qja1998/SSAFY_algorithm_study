n = int(input())
def star(n):
    if n == 3:
        return ["***", "* *", "***"]
    little = star(n // 3)
    cur = []
    for s in little:
        cur.append(s * 3)
    for s in little:
        cur.append(s + ' ' * (n // 3) + s)
    for s in little:
        cur.append(s * 3)
    return cur

print('\n'.join(star(n)))