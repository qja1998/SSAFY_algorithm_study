from collections import deque, defaultdict

INF = float('inf')
n = int(input())

nums_map = []
max_num, min_num = -INF, INF
for _ in range(n):
    row = list(map(int, input().split()))
    max_num = max(max_num, max(row))
    min_num = min(min_num, min(row))
    nums_map.append(row)

dxy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

result = INF

memo = {}

init_num = nums_map[0][0]
def bfs(l, r):
    q = deque([(0, 0)])
    visited = defaultdict(bool)
    visited[(0, 0)] = True

    while q:
        cx, cy = q.popleft()

        if not (l <= nums_map[cx][cy] <= r):
            continue

        if cx == n-1 and cy == n-1:
            memo[(l, r)] = True
            return True

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n and  0 <= ny < n):
                continue
            if visited[((nx, ny))]:
                continue

            visited[(nx, ny)] = True
            q.append((nx, ny))
    
    memo[(l, r)] = False
    return False

def bi_search(l=0, r=max_num-min_num):
    while l < r:
        mid = (l + r) // 2

        is_possible = False
        for i in range(min_num, max_num - mid + 1):
            # print(i, i+mid)
            # print(memo)
            if (i, i+mid) in memo:
                if memo[(i, i+mid)]:
                    is_possible = True
                    break
                else:
                    continue

            if bfs(i, i+mid):
                r = mid
                is_possible = True
                break

        if not is_possible:
            l = mid + 1

    return r

print(bi_search())