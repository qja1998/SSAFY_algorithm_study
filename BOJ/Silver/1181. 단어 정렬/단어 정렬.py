import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
len_cnt = [set() for i in range(51)]
for _ in range(n):
    word = input().strip()
    len_cnt[len(word)].add(word)

for words in len_cnt:
    if words:
        if len(words) == 1:
            print(f"{list(words)[0]}\n")
        else:
            for w in sorted(list(words)):
                print(f"{w}\n")