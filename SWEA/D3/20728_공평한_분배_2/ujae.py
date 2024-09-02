T = int(input())
 
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    candy_list = list(map(int, input().split()))
 
    candy_list.sort()
 
    result = set()
    for i in range(len(candy_list)-K+1):
        result.add(candy_list[i+K-1]-candy_list[i])
 
    print(f'#{test_case} {min(result)}')