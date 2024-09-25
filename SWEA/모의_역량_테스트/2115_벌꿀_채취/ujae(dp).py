def now_max_honey_dp(now_honey):
    # 선택된 꿀의 양에 따라 dp에 추가하기 위해 C+1 만큼 배열 생성
    dp = [0] * (C + 1)
    # 선택된 now_honey리스트 만큼 반복을 실행
    # 이전에 선택된 값은 다시 선택에 고려할 필요가 없으므로 이전 안에 있는 값들에 대해 접근
    for honey in now_honey:
        # 끝부터 현재까지 역순으로 dp 탐색
        # 역순으로 하는 이유 : 이미 계산된 결과값이 포함되지 않는 오류를 범하지 않기 위해
        # ex) 정방향으로 했을 경우 [3, 4, 5] 에 대해
        # dp[3] = max(dp[3], dp[3-honey]) 이고
        # dp[4] = max(dp[4], dp[4-honey]) 이고
        # dp[5] = max(dp[5], dp[5-honey]) 인 경우
        # dp5의 반복을 돌때 5는 온전한 3의 경우에 대해 계산을 수행할 수 없음, 또한 이렇게
        # 진행할 경우 동일한 계산에 대해 반복이 생길 수 있음 // dp[3]을 예로 들때 j가
        # 3일때 dp[3]이 dp[0] + 9로, j가 4일때 dp[4]가 dp[1]+9로 .. 이렇게 가다보면
        # 같은 반복에서 계산된 dp[3]이 j가 6일때 dp[3]+9로 계산되면서 중복적으로 계산이
        # 될 수 있음
        # 그렇기에 역방향을 사용합시다~, 역방향은 그런 문제가 없음
        # 왜냐면 j가 클 경우부터 접근하는데 이렇게 접근하게 되면 예를 들어서 j가 10일때
        # dp[10]에 대해서 dp[10]과 dp[7]+9 의 경우를 비교에 넣고, dp[9]에선
        # dp[9]와 dp[6]+9 의 경우를 비교해 넣고.. 이를 반복하면 계산되지 않은 이전 값에 대해
        # 계산을 수행하게 됨
        for j in range(C, honey - 1, -1):
            # 최댓값에 대해 dp 배열 갱신
            dp[j] = max(dp[j], dp[j - honey] + honey ** 2)
        # 정방향
        # for i in range(honey, C+1):
        #     dp[i+1] = max(dp[i], dp[i - honey] + honey ** 2)
    # 최댓값 반환
    return max(dp)


T = int(input())

for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    honey_info = [list(map(int, input().split())) for _ in range(N)]
    max_honey = float('-inf')

    for worker1_y in range(N):
        for worker1_x in range(N - M + 1):
            now_honey1 = honey_info[worker1_y][worker1_x:worker1_x + M]
            # dp로 해버리면 재귀를 할 필요가 없기에 리스트만 전달
            worker1_max_honey = now_max_honey_dp(now_honey1)

            for worker2_y in range(worker1_y, N):
                start_x = worker1_x + M if worker1_y == worker2_y else 0
                for worker2_x in range(start_x, N - M + 1):
                    now_honey2 = honey_info[worker2_y][worker2_x:worker2_x + M]
                    # dp로 해버리면 재귀를 할 필요가 없기에 리스트만 전달
                    worker2_max_honey = now_max_honey_dp(now_honey2)
                    max_honey = max(max_honey, worker1_max_honey + worker2_max_honey)

    print(f'#{test_case} {max_honey}')