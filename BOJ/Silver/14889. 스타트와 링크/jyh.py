from collections import deque


def find_fastest_time(N, K):
    # 범위 설정
    max_pos = 100000
    # 방문 체크와 최소 시간을 기록할 리스트 생성
    visited = [-1] * (max_pos + 1)

    # 초기 위치 설정 (수빈이 위치에서 시작)
    queue = deque([N])
    visited[N] = 0  # 시작 위치의 시간은 0

    # BFS 탐색 시작
    while queue:
        current = queue.popleft()

        # 동생의 위치에 도달하면 최소 시간을 반환
        if current == K:
            return visited[current]

        # 다음으로 이동할 세 가지 경우를 모두 확인
        for next_pos in (current - 1, current + 1, current * 2):
            # 다음 위치가 범위 내에 있고 방문하지 않은 경우
            if 0 <= next_pos <= max_pos and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)


# 입력 받기
N, K = map(int, input().split())

# 결과 출력
print(find_fastest_time(N, K))
