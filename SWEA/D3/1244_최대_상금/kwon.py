def search_prize(cards, change_num):
    if change_num == 0:
        global max_prize
        max_prize = max(max_prize, int(''.join(map(str, cards))))
        return cards


    for i in range(cards_num-1):
        for j in range(i + 1, cards_num):
            tmp_cards = cards[:]
            tmp_cards[i], tmp_cards[j] = tmp_cards[j], tmp_cards[i]
            if (change_num, tmp_cards) not in visited:
                # print(change_num, tmp_cards, visited, change_num)
                search_prize(tmp_cards, change_num - 1)
                visited.append((change_num, tmp_cards))

test_case = int(input())

for t in range(test_case):
    cards, change_num = input().split()

    cards = [int(num) for num in cards]
    cards_num = len(cards)
    change_num = int(change_num)

    max_prize = 0
    visited = []

    search_prize(cards, change_num)

    print(f"#{t + 1} {max_prize}")