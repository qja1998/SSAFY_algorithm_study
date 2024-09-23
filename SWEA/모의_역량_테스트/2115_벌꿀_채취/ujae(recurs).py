def now_max_honey(index, amount, money, now_honey):
    # 반환할 result 값
    global result
    # index == M 로 한 이유 : now_honey의 길이가 M임, 왜냐하면 M만큼의 꿀통을 선택해야 하기 때문
    # 그렇기에 index == M 이라면 주어진 now_honey를 다 돌고 다시 돌아온 경우임
    # 추가적으로 설명하자면, index의 범위는 0~M-1, 재귀로 현재 주어진 리스트에 대해 최대 이익을 판별하기 때문에 모든 경우를 다 돌고
    # 탈출 조건으로 왔을때는 index==M이 됨, 만약 index==M-1로 했다면 리스트의 마지막 값에 대해 판별을 하지 않음
    if index == M:
        # C는 일꾼 한 명이 최대로 선택할 수 있는 꿀의 양, 만약 amount가 C를 초과한다면 조건을 만족하지 않기에 바로 return
        if amount <= C:
            # 지금까지 재귀를 돌았을때 나온 money가 result보다 크다면 현재의 선택이 최선의 선택이기에 result 갱신
            if result < money:
                result = money
        return
    # 현재 index의 꿀통을 선택하지 않고 다음 꿀통부터 선택함, 그렇기에 amount, money에 대해 변화가 없음
    now_max_honey(index + 1, amount, money, now_honey)
    # 현재 index의 꿀통을 선택함, 그렇기에 주어진 리스트 now_honey에서 해당 index의 꿀 양을 amount에 더해주고
    # money에 해당 꿀통의 꿀 양의 제곱을 더해줌
    now_max_honey(index + 1, amount + now_honey[index], money + now_honey[index] ** 2, now_honey)


# 테스트 케이스 갯수 받아오기
T = int(input())
# 테스트 케이스 갯수 만큼 반복
for test_case in range(1, T + 1):
    # N, M, C 입력받기 : N(벌통의 크기 N*N), M(한 명의 일꾼이 선택할 수 있는 벌통의 갯수, 같은 열에서만 선택 가능)
    # C(한 명의 일꾼이 채취할 수 있는 꿀의 양)
    N, M, C = map(int, input().split())
    # honey_info : N만큼 각 벌통들에 담긴 꿀의 정보 입력받기
    honey_info = [list(map(int, input().split())) for _ in range(N)]
    # max_honey를 -inf로 하여 max로 비교해 선택되는 꿀통들의 값이 선택되도록 함
    max_honey = float('-inf')
    # 완탐을 위해 일꾼1 부터 범위 설정하기, y에 대해 전체 범위를 돌아야 함
    for worker1_y in range(N):
        # 완탐을 위해 일꾼1 부터 범위 설정하기, x가 가능한 범위는 N-M+1임
        # N-M+1 인 이유 : for 문의 끝 반복 값은 포함하지 않고 범위의 -1까지만 반복 됨
        # 그렇기에 마지막 자리까지 포함하기 위해서는 +1을 해줘야함
        # ex) N=5, M=3 이면 선택할 수 있는 범위가 (0,1,2), (1,2,3), (2,3,4) 이때 (2,3,4)에 대해 돌기 위해서는
        # 5-3=2 , 2+1=3, range(3)을 해야 0,1,2 에 대해 반복문을 실시함
        for worker1_x in range(N - M + 1):
            # result를 함수 밖에서 선언하지 않고 def로 만든 함수 내부에서 변수를 만들고 이를 return 하면 밖의 변수에 값이 담기지 않음
            # 그래서 외부에서 변수를 만들고 global로 def로 만든 함수 내에서도 변수를 실행할 수 있게 한 다음 return 값에는 따로 변수를
            # 담지 않고 함수의 반복을 끝내는 용도로 사용
            ###################################### 근데 왜 def 함수 내부의 변수를 return 하면 None이 담기는 가?
            ###################################### ex) result = bfs(변수, 변수, 변수 ~~~)
            ########################################## def bfs(변수, ....)
            ##########################################    sol = 0
            ##########################################    return sol
            result = 0
            # now_max_honey 함수 돌리기 now_max_honey(현재 접근하는 index, 현재 선택한 꿀의 양, 해당 꿀을 선택함으로써 얻는 이득, 선택한 꿀 리스트)
            # 주어진 인자값 (마지막으로 주어진 리스트에 대해 접근하는 인덱스, 현재 재귀에서 선택된 꿀의 양, 선택된 꿀로 계산한 이익, 주어진 리스트)
            now_max_honey(0, 0, 0, honey_info[worker1_y][worker1_x:worker1_x + M])
            # 현재 해당하는 반복에서 일꾼1이 선택한 꿀 리스트에서 얻을 수 있는 최대 이익
            worker1 = result
            # 일꾼 1이 선택한 범위 부터 끝까지 돌면 됨, 일꾼1이 선택하고 그 뒤의 나머지 공간에 대해 일꾼2가 탐색하도록 했기 때문
            for worker2_y in range(worker1_y, N):
                # pan : 현재 일꾼1과 일꾼2가 선택한 행이 같은 행인가 (y 좌표에 대해)
                pan = 0
                # 만약 두 명의 일꾼이 선택한 꿀통 리스트의 y좌표 값이 같다면 x좌표의 시작 값이 일꾼1이 선택한 x좌표에서
                # 가로로 이어지게 꿀을 M만큼 선택해야 하므로, worker1_x + M을 통해 그 이후의 값부터 선택하도록 함
                # worker1_x + M +1이 아닌 이유는 선택하는 갯수는 시작 위치의 갯수도 포함해야 하기에 +M만 해주면 됨
                if worker1_y == worker2_y:
                    pan = worker1_x + M
                for worker2_x in range(pan, N - M + 1):
                    # 위에서 일꾼 1의 경우와 마찬가지로 외부에서 변수를 선언해주고 함수에서 해당 변수를 global로 계산함
                    result = 0
                    # 주어진 인자값 (마지막으로 주어진 리스트에 대해 접근하는 인덱스, 현재 재귀에서 선택된 꿀의 양, 선택된 꿀로 계산한 이익, 주어진 리스트)
                    now_max_honey(0, 0, 0, honey_info[worker2_y][worker2_x:worker2_x + M])
                    # 현재 해당하는 반복에서 일꾼2이 선택한 꿀 리스트에서 얻을 수 있는 최대 이익
                    worker2 = result
                    # 결과 값에 대해 최대로 이익을 보는 경우를 원했기 때문에 완탐을 통해 처음부터 끝까지 각각의 모든 경우에 대해 계산 후
                    # 최대 값이 되는 결과를 max로 비교해 결과 출력 변수에 담음
                    max_honey = max(max_honey, worker1 + worker2)
    # 결과 출력
    print(f'#{test_case} {max_honey}')