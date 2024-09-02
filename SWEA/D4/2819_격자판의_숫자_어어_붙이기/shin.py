def dfs(x, y, numLen):
    # 범위 벗어날때 함수 벗어남
    if not (0 <= x < 4 and 0 <= y < 4):
        return
    # 숫자가 문자형태이기에 바로 더함
    numLen += grid[x][y]
    # 숫자 문자열의 길이가 7이되면 세트에 추가하고 함수 벗어나기
    if len(numLen) == 7:
        result.add(numLen)
        return

    dfs(x-1,y,numLen)
    dfs(x+1,y,numLen)
    dfs(x,y-1,numLen)
    dfs(x,y+1,numLen)

T = int(input())
for tc in range(1, T+1):
    grid = [list(input().split()) for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, "")
    print(f"#{tc} {len(result)}")
