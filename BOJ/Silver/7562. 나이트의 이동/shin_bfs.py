from collections import deque

dir_night = [(2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]


def bfs(c_x, c_y):
    check_arr[c_x][c_y] = 1
    queue = deque([(c_x, c_y)])
    while queue:
        current_x, current_y = queue.popleft()
        if current_x == end_ci and current_y == end_cj:
            return check_arr[current_x][current_y] - 1
        for dx, dy in dir_night:
            nx = current_x + dx
            ny = current_y + dy
            if 0 <= nx < n and 0 <= ny < n and check_arr[nx][ny] == 0:
                queue.append((nx, ny))
                check_arr[nx][ny] = check_arr[current_x][current_y] + 1


test_case = int(input())
for _ in range(test_case):
    n = int(input())
    check_arr = [[0]*n for _ in range(n)]
    start_ci, start_cj = map(int, input().split())
    end_ci, end_cj = map(int, input().split())
    print(bfs(start_ci, start_cj))
