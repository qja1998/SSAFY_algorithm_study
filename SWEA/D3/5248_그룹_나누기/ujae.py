def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]
 
 
T = int(input())
 
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    pair = list(map(int, input().split()))
    pair_list = []
 
    for i in range(int(len(pair) / 2)):
        pair_list.append((pair[2 * i], pair[2 * i + 1]))
 
    p = [i for i in range(N+1)]
 
    for a, b in pair_list:
        p[find_set(a)] = find_set(b)
 
    count = 0
    for j in range(1, N+1):
        if j == p[j]:
            count += 1
    print(f'#{test_case} {count}')