from collections import deque
import math

move = ((-1, 0), (1, 0), (0, 1), (0, -1))
def bfs():
    for y in range(N):
        for x in range(N):
            if pan_status[y][x] == 0:
                if (y, x) not in zero_list:
                    zero_list.append((y, x))
                    queue = deque([(y, x)])
                    count = 0
                    while queue:
                        count += 1
                        now_y, now_x = queue.popleft()
                        for dy, dx in move:
                            ny = now_y + dy
                            nx = now_x + dx
                            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in zero_list:
                                if pan_status[ny][nx] == 0:
                                    queue.append((ny, nx))
                                    zero_list.append((ny, nx))

                    result.append(count)

# N * N 칸으로 이루어진 나무판
# M개의 버섯 포자
# K개의 연결된 칸 -> 이 때 칸들은 적어도 한 변을 공유하고 있음
# 한 칸에 x개의 버섯 포자를 겹쳐 심으면, 포자가 심어진 칸을 포함해 최대 x * K 개의 연결된 칸에 버섯이 자람
# 버섯이 자랄 수 있는 칸 : 0, 자랄 수 없는 칸 : 1
N, M, K = list(map(int, input().split()))
pan_status = [list(map(int, input().split())) for _ in range(N)]

zero_list = []
result = []

bfs()

real_result = []
for i in result:
    real_result.append(math.ceil(i/K))

real_real_result = M - sum(real_result)
if real_real_result < 0 or real_real_result == M:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
    print(real_real_result)
