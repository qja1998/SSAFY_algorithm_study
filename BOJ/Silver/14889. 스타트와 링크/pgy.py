import sys
sys.stdin = open('input.txt', 'r')

N = int(input().strip())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(count, idx):
    global min_res

    if count == N // 2: # 한 팀에 N//2명 선택되면 시작하기
        start_score = 0
        link_score = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]: # 먼저 선택된 쌍 => 스타트팀
                    start_score += arr[i][j]
                elif not visited[i] and not visited[j]: # 나머지는 링크팀
                    link_score += arr[i][j]
        min_res = min(min_res, abs(start_score - link_score))
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True # 방문처리하고
            dfs(count + 1, i + 1) # dfs 돌린 후에
            visited[i] = False # 다시 복구해주기

min_res = float('inf')
visited = [False] * N

dfs(0, 0)
print(min_res)
