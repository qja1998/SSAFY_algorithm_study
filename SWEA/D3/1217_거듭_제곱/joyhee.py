import sys
sys.stdin = open("input (1).txt", 'r')

# 주어진 입력 받기
for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    # 제곱 반복_곱할거라서 초기값이 0이 아니라 1
    ans = 1
    for _ in range(M):
        ans *= N
    print(f'#{tc} {ans}')