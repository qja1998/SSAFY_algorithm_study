import sys
sys.stdin = open('14719.txt', 'r')

# 입력받기
T = int(input())
for tc in range(T):
    H, W = map(int, input().split())
    li = list(map(int, input().split()))

    ans = 0
    for i in range(1, W - 1):
        # 앞부터 가장 높은 벽 찾아주기
        least_deep = max(li[:i])
        # 가장 높은벽 뒤부터 가장 높은 벽 찾아주기
        deep = max(li[i+1:])
        # 채울 수 있는 높이 확인하기
        Precipitation = min(least_deep, deep)
        # 벽이랑 같은 높이가 아니라면 결과에 더하기
        if li[i] < Precipitation:
            ans += Precipitation - li[i]
    # 정답 출력
    print(ans)