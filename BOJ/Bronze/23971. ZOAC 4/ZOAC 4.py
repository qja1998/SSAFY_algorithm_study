h, w, n, m = map(int, input().split())

result = ((h - 1) // (n + 1) + 1) * ((w - 1) // (m + 1) + 1)

print(result)