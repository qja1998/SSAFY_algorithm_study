# 마지막 글자가 첫 번째와 두 번째 사이로 이동
# 뒤에서 두 번째 글자가 두 번째 글자와 세번째 글자 사이로
# 뒤에서 k번째는 앞에서부터 k~k+1로 진행

import math

def suffle(s):
    s_list = list(s)
    split_i = math.ceil(len(s)/2)
    front = list(s[:split_i])
    back = list(s[split_i:])[::-1]

    s_list[::2] = front
    s_list[1::2] = back

    return ''.join(s_list)

def search(s):
    origin_s = s

    word_list = [origin_s]
    while True:
        s = suffle(s)
        if origin_s == s:
            break
        word_list.append(s)

    return len(word_list), word_list

X = int(input())
s = input()

cnt, word_list = search(s)
print(word_list[::-1][X % cnt - 1])