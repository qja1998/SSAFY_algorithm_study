from collections import deque, defaultdict

T = int(input())

dxy = [[1, 2], [-1, 2], [1, -2], [-1, -2],
       [2, 1], [-2, 1], [2, -1], [-2, -1]]

def search(start, target, bound):
    global dxy

    q = deque([(start, 0)])
    visited = defaultdict(bool)
    visited[start] = True
    while q:
        (x, y), cnt = q.popleft()
        if (x, y) == target:
            return cnt
        
        for dx, dy in dxy:

            nx, ny = x + dx, y + dy
            if not(0 <= nx < bound and 0 <= ny < bound):
                continue
            if visited[(nx, ny)]:
                continue
            q.append([(nx, ny), cnt+1])
            visited[(nx, ny)] = True

for t in range(T):
    I = int(input())

    start = tuple(map(int, input().split()))
    target = tuple(map(int, input().split()))

    print(search(start, target, I))