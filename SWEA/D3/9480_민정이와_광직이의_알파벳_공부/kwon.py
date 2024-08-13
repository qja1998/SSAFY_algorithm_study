test_case = int(input())

answer = set("abcdefghijklmnopqrstuvwxyz")

def search(words, words_set):
    global cnt
    if not words:
        chk_cnt = 0
        for c in list(set(words_set)):
            if c in answer:
                chk_cnt += 1

        if chk_cnt == 26:
            cnt += 1
    for i, word in enumerate(words):
        search(words[i+1:], words_set + word)

for t in range(test_case):
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    
    words += ['']
    words_set_list = []

    cnt = 0

    search(words, '')
    print(f"#{t+1} {cnt}")