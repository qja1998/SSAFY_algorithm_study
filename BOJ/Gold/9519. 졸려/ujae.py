def change_word(word):
    result = ""
    if len(word) % 2 == 0:
        result += word[::2]
        result += word[-1::-2]
    else:
        result += word[::2]
        result += word[-2::-2]
    return result


X = int(input())
word = input()
word_list = []

for j in range(X):
    word = change_word(word)
    if word in word_list:
        word = word_list[X % len(word_list) - 1]
        break
    else:
        word_list.append(word)

print(word)
