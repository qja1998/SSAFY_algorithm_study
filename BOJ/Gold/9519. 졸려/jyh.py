# 입력
x = int(input())
li = input()

dict = {}  # 이전에 등장한 단어와 그때의 순서를 기록하기 위한 딕셔너리
cycle = []  # 변경된 단어들을 저장할 리스트

k = len(li)//2

# x번 또는 반복이 발견될 때까지
for i in range(x):
    # 현재 단어가 이미 이전에 등장한 경우
    if li in dict:
        # 반복시작점 잡기
        cycle_st = i - dict[li]
        # 남은 x수 / 반복길이 나머지만큼만 계산하면 된다.
        remaining_blinks = (x - i) % cycle_st
        print(cycle[remaining_blinks])  # 남은 연산 횟수만큼 이동한 결과 출력
        break
    # 처음보는 단어라면 단어와 위치 dict에 저장, 리스트에 추가
    dict[li] = i
    cycle.append(li)

    # 단어 리스트로 만들어서 자리바꾸기
    result = list(li)
    # 맨뒤부터 시작
    for j in range(k - 1, -1, -1):
        # 인덱스 위치에 있는 문자를 리스트의 마지막으로 이동
        result.append(result.pop(j * 2 + 1))
    # 리스트를 다시 문자열로 변환하여 li에 저장
    li = ''.join(result)
else:
    # x번 반복한 후 반복이 발견되지 않은 경우
    print(li)