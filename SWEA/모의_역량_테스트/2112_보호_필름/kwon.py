test_case = int(input())

def chk_test():
    chk_a_list = [0] * k
    chk_b_list = [1] * k

    for w_i in range(w):
        is_success = False
        for d_i in range(d - k):
            cur_chk = [film[tmp_i][w_i] for tmp_i in range(d_i, d_i + k)]
            if cur_chk == chk_a_list or cur_chk == chk_b_list:
                is_success = True
                break
        if not is_success:
            return False
    return True

def inject(depth, inject_list):
    film[depth] = inject_list

def test_film(film, depth=0, cnt_inject=0):
    global min_inject
    if depth == d:
        return
    if chk_test():
        min_inject = min(min_inject, cnt_inject)
        return

    # 현재 층을 그대로
    test_film(film, depth + 1, cnt_inject)

    # 현재 층을 a로
    origin_membrane = film[depth][:]

    inject(depth, inject_a)
    test_film(film, depth + 1, cnt_inject + 1)
    # 원래대로 복구
    inject(depth, origin_membrane)

    # 현재 층을 b로
    inject(depth, inject_b)
    test_film(film, depth + 1, cnt_inject + 1)

for t in range(test_case):
    d, w, k = map(int, input().split())

    film = [list(map(int, input().split())) for _ in range(d)]
    
    inject_a = [0] * w
    inject_b = [1] * w

    min_inject = float('inf')

    test_film(film)
    print(f"#{t + 1} {min_inject}")