TC = int(input())

def search_string(string, target):
    i = 0
    cnt = 0
    string_len = len(string)
    target_len = len(target)
    while i < string_len-target_len:
        if string[i] != target[0]:
            i += 1
            continue
        if string[i:i+target_len] == target:
            cnt += 1
        i += 1
    return cnt
    
for t in range(1, TC+1):
    target = input()
    string = input()
    print(f"#{t} {search_string(string, target)}")