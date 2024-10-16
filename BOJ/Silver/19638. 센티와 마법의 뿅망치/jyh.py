import heapq

def giant_hammer(N, tall, T, li):
    # 최대 힙을 만들기 위해 거인의 키를 음수로 저장
    max_heap = [-h for h in li]
    # 거인의 키를 저장한 리스트를 힙으로 변환
    heapq.heapify(max_heap)
    used_hammer = 0  # 마법의 뿅망치를 사용한 횟수를 저장하는 변수

    # 마법의 뿅망치를 최대 T번 사용할 수 있으므로 T번 반복
    for _ in range(T):
        # 현재 가장 키가 큰 거인을 양수로 힙에서 꺼냄
        tallest = -heapq.heappop(max_heap)

        # 만약 현재 가장 큰 거인의 키가 센티보다 작다면 더 이상 마법을 사용할 필요가 없으므로 종료
        if tallest < tall:
            # 거인의 키가 모두 센티보다 작아졌으므로 YES를 출력하고, 사용한 마법 횟수를 반환
            return "YES", used_hammer

        # 거인의 키가 1이면 더 이상 줄일 수 없으므로 종료
        if tallest == 1:
            # 힙에 1을 다시 넣지 않음
            heapq.heappush(max_heap, -1)
            continue

        # 거인의 키를 절반으로 줄임
        new_height = tallest // 2
        # 줄어든 키가 1 이상인 경우에만 힙에 다시 삽입
        if new_height > 1:
            heapq.heappush(max_heap, -new_height)
        else:
            # 줄어든 키가 1이면 힙에 1을 다시 넣음
            heapq.heappush(max_heap, -1)

        # 마법의 뿅망치를 사용했으므로 횟수 증가
        used_hammer += 1

    # T번의 뿅망치를 모두 사용한 후에도 가장 큰 거인의 키가 센티보다 크거나 같으면 NO를 출력
    if -max_heap[0] >= tall:
        # NO와 함께 현재 거인 중 키가 가장 큰 값을 출력
        return "NO", -max_heap[0]
    else:
        # 만약 모든 거인의 키가 센티보다 작다면 YES를 출력하고, 사용한 마법 횟수를 반환
        return "YES", used_hammer

# 입력
N, tall, T = map(int, input().split())
li = [int(input()) for _ in range(N)]

# 마법의 뿅망치를 사용한 결과를 함수로 계산
result, value = giant_hammer(N, tall, T, li)

# 결과 출력
print(result)
print(value)