import sys
sys.stdin = open("input.txt", "r")

# 주어진 입력 받기
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]

    # 마름모 돌기
    ans = 0
    cnt = 1
    mid = N//2
    # 한 줄씩
    for harvest in range(N):
        # 가운데 확인
        ans += farm[harvest][mid]
        # 양 옆을 한자리씩 확인
        for repeat in range(1, cnt):
            ans += farm[harvest][mid + repeat]
            ans += farm[harvest][mid - repeat]
        # 확인할 사이즈 늘리기
        cnt += 1
        # 절반 넘었으면 다시 사이즈 줄이기
        if harvest >= mid:
            cnt -= 2
    # 정답 출력
    print(f"#{tc} {ans}")