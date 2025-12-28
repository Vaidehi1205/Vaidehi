"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card."""

    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)


def higher_card(card_one, card_two):
    """Determine which card has the higher value in the hand."""

    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 > v2:
        return card_one
    elif v2 > v1:
        return card_two
    else:
        return (card_one, card_two)


def value_of_ace(card_one, card_two):
    def card_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        if card == 'A':
            return 11
        return int(card)

    # If we already have an Ace in hand → new ace must be 1
    if card_one == 'A' or card_two == 'A':
        return 1

    # Calculate total if we choose ace = 11
    total_with_ace = card_value(card_one) + card_value(card_two) + 11

    # If bust, ace must be 1
    if total_with_ace > 21:
        return 1
    return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a natural blackjack."""

    def blackjack_value(card):
        if card in ['J', 'Q', 'K']:
            return 10
        if card == 'A':
            return 11
        return int(card)

    total = blackjack_value(card_one) + blackjack_value(card_two)
    return total == 21


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand."""

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if the hand total is 9, 10, or 11 (double-down condition)."""

    total = value_of_card(card_one) + value_of_card(card_two)
    return total in (9, 10, 11)
