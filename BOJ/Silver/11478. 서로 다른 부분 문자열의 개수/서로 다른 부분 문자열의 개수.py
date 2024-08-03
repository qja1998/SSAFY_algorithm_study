s = input().strip()
n = len(s)
sub_dict = {}
for i, c in enumerate(s):
    for j in range(i + 1, n + 1):
        sub_str = s[i:j]
        if sub_str not in sub_dict:
            sub_dict[sub_str] = True
print(len(sub_dict))