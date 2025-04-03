JOKER = 0

def solution(cards):
    jokers = cards.count(JOKER)
    cards = sorted(set(cards))

    if jokers > 0:
        cards.remove(JOKER)

    max_length = 0
    left = 0
    right = 1

    while right < len(cards):
        # (cards[right] - cards[left] + 1) - expected sequence size
        # (right - left + 1) - actual sequence size
        while (cards[right] - cards[left]) - (right - left) > jokers:
            left += 1

        current_length = right - left + 1
        max_length = max(max_length, current_length)
        right += 1

    return max_length + jokers
