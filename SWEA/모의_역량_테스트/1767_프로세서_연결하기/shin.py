# 전선을 놓을 수 있는지 확인하는 함수
def can_place_wire(grid, x, y, direction):
    N = len(grid)  # 그리드의 크기
    dx, dy = direction  # 전선이 놓일 방향
    nx, ny = x + dx, y + dy  # 전선이 놓일 다음 좌표
    while 0 <= nx < N and 0 <= ny < N:  # 그리드 범위 내에서
        if grid[nx][ny] != 0:  # 전선이 놓일 자리에 다른 전선이나 코어가 있으면
            return False  # 전선을 놓을 수 없음
        nx += dx
        ny += dy
    return True  # 전선을 놓을 수 있음


# 전선을 놓거나 제거하는 함수
def place_wire(grid, x, y, direction, value):
    N = len(grid)  # 그리드의 크기
    dx, dy = direction  # 전선이 놓일 방향
    nx, ny = x + dx, y + dy  # 전선이 놓일 다음 좌표
    length = 0  # 전선의 길이
    while 0 <= nx < N and 0 <= ny < N:  # 그리드 범위 내에서
        grid[nx][ny] = value  # 전선을 놓거나 제거함
        nx += dx
        ny += dy
        length += 1  # 전선의 길이를 증가시킴
    return length  # 놓인 전선의 전체 길이를 반환


# DFS를 통해 최대한 많은 코어에 전원을 연결하는 함수
def dfs(idx, connected, total_length):
    global max_connected, min_length, core_crd, mexinos  # 전역 변수 사용

    if idx == len(core_crd):  # 모든 코어를 다 확인한 경우
        if connected > max_connected:  # 더 많은 코어가 연결된 경우
            max_connected = connected  # 최대 연결된 코어 수 갱신
            min_length = total_length  # 전선 길이 갱신
        elif connected == max_connected:  # 연결된 코어 수가 동일한 경우
            min_length = min(min_length, total_length)  # 최소 전선 길이 갱신
        return

    x, y = core_crd[idx]  # 현재 확인할 코어의 좌표
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향

    # 현재 코어를 연결하지 않는 경우
    dfs(idx + 1, connected, total_length)

    # 현재 코어를 연결하는 경우
    for direction in directions:
        if can_place_wire(mexinos, x, y, direction):  # 전선을 놓을 수 있으면
            length = place_wire(mexinos, x, y, direction, 2)  # 전선을 놓음
            dfs(idx + 1, connected + 1, total_length + length)  # 다음 코어로 이동
            place_wire(mexinos, x, y, direction, 0)  # 원상복귀 (전선을 제거)


# 메인 실행 부분
T = int(input())  # 테스트 케이스의 수를 입력받음
for tc in range(1, T + 1):  # 각 테스트 케이스에 대해
    N = int(input())  # 그리드의 크기를 입력받음
    mexinos = [list(map(int, input().split())) for _ in range(N)]  # 그리드를 입력받음
    core_crd = [(i, j) for i in range(N) for j in range(N) if
                i != 0 and i != N - 1 and j != 0 and j != N - 1 and mexinos[i][j] == 1]
    # 가장자리를 제외한 코어의 좌표를 추출

    max_connected = 0  # 최대 연결된 코어 수 초기화
    min_length = float('inf')  # 최소 전선 길이 초기화

    dfs(0, 0, 0)  # DFS 호출

    print(f"#{tc} {min_length}")  # 결과 출력
