def palindrome(word):
    if len(word) < 2:
        return 1
    if word[0] != word[-1]:
        return 0
    return palindrome(word[1:-1])

T = int(input())
for ts in range(1 , T+1):
    print(f"#{ts} {palindrome(input())}")
