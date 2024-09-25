def word_re(word):
    if word==[]:
        return 1
    elif word[0] != word[len(word)-1] or len(word)==1:
        return 0
    else:
        word.pop()
        word.reverse()
        word.pop()
        word_re(word)
        return 1
 
T = int(input())
 
for test_case in range(1, T + 1):
    word = list(input())
    print(f"#{test_case} {word_re(word)}")
