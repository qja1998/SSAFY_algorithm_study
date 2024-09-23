def check():
    for a1 in range(W):
        now_drug = film[0][a1]
        pan = 0
        for z in range(D):
            if film[z][a1] == now_drug:
                pan += 1
            else:
                now_drug = film[z][a1]
                pan = 1
            if pan >= K:
                break
        if pan < K:
            return False
    return True
 
 
def drug(count, i):
    global min_count
    if check():
        min_count = min(min_count, count)
        return min_count
 
    if i >= D or count >= min_count:
        return
 
    original_film = film[i][:]
    drug(count, i+1)
    for w1 in range(W):
        film[i][w1] = 1
    drug(count+1, i+1)
    for w2 in range(W):
        film[i][w2] = 0
    drug(count+1, i+1)
    for w3 in range(W):
        film[i][w3] = original_film[w3]
 
 
T = int(input())
 
for test_case in range(1, T+1):
    D, W, K = list(map(int, input().split()))
    film = [list(map(int, input().split())) for _ in range(D)]
    min_count = float('inf')
    drug(0, 0)
 
    print(f"#{test_case} {min_count}")