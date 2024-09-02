import sys
sys.stdin = open('input.txt', 'r')

# 주어진 입력 받기
T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input(). split())
    # M을 이진수로 바꾸고, 3째자리(2번인덱스)부터 남기기_0이랑 1은 형식번호
    bin_M = bin(M)[2:]
    # 기본은 켜져있음. 이후 조건 충족 여부 확인하여 OFF로 갱신
    ans = 'ON'
    # N이 이진수 길이보다 길다면, 0으로 채워져 있으니까 OFF
    if N > len(bin_M):
        ans = 'OFF'
    else :
        # N 개의 비트 확인
        for i in range(1, N+1):
            # 하나라도 0이면 OFF로 바꾸고 끝내기
            if bin_M[-i] == '0':
                ans = 'OFF'
                break
    # 정답 출력
    print(f'#{tc} {ans}')