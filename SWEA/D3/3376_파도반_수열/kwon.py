padoban = [0, 1, 1, 1, 2, 2, 3, 4]

TC = int(input())

for t in range(1, TC+1):
    n = int(input())
    if n <= 7:
        print(f"#{t} {padoban[n]}")
        continue
    padoban += [0] * (n-7)
    for i in range(8, n+1):
        padoban[i] = padoban[i-1] + padoban[i-5]
    
    print(f"#{t} {padoban[n]}")

# 규칙 더 있음
t = int(input())
arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11,101):
    arr.append(arr[i-2]+arr[i-3])

for _ in range(t):
    n = int(input())
    print(arr[n])