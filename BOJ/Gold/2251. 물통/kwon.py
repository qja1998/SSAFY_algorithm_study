A, B, C = map(int, input().split())

result = list(set([
    A,
    C-A,
    B,
    C-B,
    C
]))



print(*sorted(result))