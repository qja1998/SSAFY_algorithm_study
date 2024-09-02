import itertools
  
T = int(input())
  
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    for i in range(len(A)):
        if A[i] > K:
            A = A[:i]
            break
              
    count = 0
    for i in range(len(A)):
        B = itertools.combinations(A,i)
        for j in B:
            if sum(j) == K:
                count += 1
  
    print(f'#{test_case} {count}')