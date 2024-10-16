from collections import deque

move = ((-1, 0), (1, 0), (0, -1), (0, 1))

def find_danzi(y, x):
    queue = deque([(y, x)])
    count = 1
    while queue:
        now = queue.popleft()
        for dy, dx in move:
            ny = dy + now[0]
            nx = dx + now[1]
            if 0 <= ny < N and 0 <= nx < N and ((ny, nx) not in found_danzi):
                if danzi_info[ny][nx] == 1:
                    queue.append((ny, nx))
                    found_danzi.append((ny, nx))
                    count += 1
    return count

N = int(input())
danzi_info = [list(map(int, input().rstrip())) for _ in range(N)]

found_danzi = []
result = []

for y in range(N):
    for x in range(N):
        if (y, x) in found_danzi or danzi_info[y][x] == 0:
            continue
        else:
            found_danzi.append((y, x))
            here = find_danzi(y, x)
            result.append(here)

result.sort(reverse=False)
print(len(result))
print("\n".join(map(str, result)))
