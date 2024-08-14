import sys
sys.stdin = open("sample_input.txt", "r")

from collections import deque
T = int(input())
for tc in range(1, 1+T):
    N, K = map(int, input().split())
    numli = deque(input())

    # 한 줄에 몇 자리씩 들어가는지
    cnt = N//4
    # 비교할 비밀번호 세트
    numset = set()

    # N회전 돌면서 맨앞 지우고 맨뒤에 넣기
    for _ in range(cnt):
        for num in range(4):
            b = '0x'
            for a in range(num*cnt, num*cnt+cnt):
                b += numli[a]
            numset.add(b)
        numli.append(numli.popleft())

    # 10진수로 바꾸기
    decimalli = []
    for i in range(len(numset)):
        decimalli.append(int(numset.pop(), 16))
    decimalli.sort(reverse=True)
    # K번째, 인덱스로 K-1번째 수 확인
    ans = decimalli[K-1]

    print(f"#{tc} {ans}")