# 입력값 받기, N : 일 할 수 있는 일수 , counsel : T(일 걸리는 시간), P(버는 돈)
N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]
# 0번째 인덱스는 사용 X, 벌어들이는 돈을 일 걸리는 시간 다음날에 저장할 것이기 때문에 +2,
# 마지막 날의 결과를 저장하기 위함
cost = [0] * (N+2)

# 1, len(counsel)+1 도는이유 : 계산하기 편하기 위해
for i in range(1, len(counsel)+1):
    # T, P의 값들을 하나씩 순서대로 넣어주고
    T = counsel[i-1][0]
    P = counsel[i-1][1]
    # T+i = 일을 끝낸 다음날, N+1 = 내가 일을 끝내야 하는 마지노선,
    # i를 1부터 시작하고 len(counsel)+1 범위까지 가기 때문에 N+1이 가능함
    if T+i <= N+1:
        # cost i+T 자리에, 기존에 있던 cost[i+T] 와 새로운 값 cost[:i+1] 중의 최대에 P를 더한 값 중 더 큰 값 넣기
        # => 이 말은 즉, 현재 있는 날짜(i-1)에서 T일 만큼 지났을때 의 위치에 넣는 것,
        # => 그리고 i+1인 이유는 현재 일 수 부터 전에 있던 cost 중에서 최대값이랑 현재의 이득 P랑 더하는것
        # => i+T는 내가 일을 끝낸 다음날, i+1은 i까지의 범위를 포함하니까 가능
        cost[i+T] = max(cost[i+T], max(cost[:i+1])+P)
    else:
        continue
# 출력
print(max(cost))