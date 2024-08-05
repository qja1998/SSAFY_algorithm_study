test_case = int(input())

def chk_test():
    chk_a_list = [0] * k
    chk_b_list = [1] * k

    for w_i in range(w):
        is_success = False
        for d_i in range(d - k + 1):
            cur_chk = [film[tmp_i][w_i] for tmp_i in range(d_i, d_i + k)]
            if cur_chk == chk_a_list or cur_chk == chk_b_list:
                is_success = True
                break
        if not is_success:
            return False
    return True

def test_film(film, depth=0, cnt_inject=0, chk_list=[]):
    global min_inject
    
    if cnt_inject >= min_inject:
        return

    # if len(chk_list) == d:
    #     for row in film:
    #         print(row)
    #     print(chk_test(), cnt_inject, chk_list)

    if chk_test():
        min_inject = min(min_inject, cnt_inject)
        return

    if depth >= d:
        return
    
    origin_membrane = film[depth][:]

    # 현재 층을 그대로
    test_film(film, depth + 1, cnt_inject, chk_list + ['0'])

    # 현재 층을 a로
    film[depth] = inject_a
    test_film(film, depth + 1, cnt_inject + 1, chk_list + ['a'])
    film[depth] = origin_membrane

    # 현재 층을 b로
    film[depth] = inject_b
    test_film(film, depth + 1, cnt_inject + 1, chk_list + ['b'])
    film[depth] = origin_membrane

for t in range(test_case):
    d, w, k = map(int, input().split())

    film = [list(map(int, input().split())) for _ in range(d)]
    
    inject_a = [0] * w
    inject_b = [1] * w

    min_inject = float('inf')

    test_film(film)
    print(f"#{t + 1} {min_inject}")