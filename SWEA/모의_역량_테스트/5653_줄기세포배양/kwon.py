from collections import defaultdict, deque

test_case = int(input())
dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dict_init():
    return (-1, -1, False)

for t in range(test_case):
    n, m, k = map(int, input().split())

    matrix = defaultdict(dict_init)

    q = deque()
    for y in range(n):
        for x, num in enumerate(map(int, input().split())):
            matrix[(x, y)] = [num, num, False]
            q.append([x, y, num, num, False])

    # 생명력: X시간 비활성 -> X시간 활성 -> 죽음
    # 이미 있는 경우 번식 x
    # 동시 번식은 생명력 높은 애가

    
    print('q:', q)
    for _ in range(k):
        # 시작할 수 있는 세포가 나올 때까지 반복
        while True:
            (x, y, start_num, end_num, is_move) = q[0]
            # 움직이기 전이라고 표시
            if end_num and is_move:
                is_move = False
            if start_num == 0:
                q[0][2] -= 1
                matrix[(x, y)][0] -= 1
                q.append(q.popleft())
                continue
            break

        x, y, start_num, end_num, is_move = q.popleft()

        # 딕셔너리와 다르면 이미 먹힌 것
        if [start_num, end_num, is_move] != matrix[(x, y)]:
            continue

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            n_start_num, n_end_num, n_is_move = matrix[(nx, ny)]

            # 움직이기 전 세포로는 번식 못함
            if not n_is_move:
                continue
            
            # 생명력이 더 크다면 번식 가능
            if n_end_num < num:
                # 죽음
                if end_num-1 == 0:
                    matrix[(nx, ny)] = -1, -1, False
                    continue
                q.append([nx, ny, start_num, end_num-1, True])
                matrix[(nx, ny)] = start_num, end_num-1, True

    for xy in matrix:
        print(xy)
        # print(matrix[xy])

    print(f"#{t+1} {len(matrix)}")