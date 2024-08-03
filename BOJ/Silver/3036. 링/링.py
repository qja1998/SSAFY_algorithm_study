n = int(input())
ring = list(map(int, input().split()))
first = ring[0]
rings = ring[1:]
def gcd(a, b):
    while a % b != 0:
        r = a % b
        a, b = b, r
    return b

for r in rings:
    if first % r == 0:
        print(f"{first // r}/1")
    elif r % first == 0:
        print(f"1/{r // first}")
    else:
        g = gcd(first, r)
        print(f"{first // g}/{r // g}")
