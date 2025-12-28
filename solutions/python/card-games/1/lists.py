"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    n=int(number)
    n1=n+1
    n2=n+2
    round = [n , n1 , n2]
    
    return round

    pass


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    rounds = rounds_1+rounds_2
    return rounds

    pass


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    n=int(number)

    return n in rounds

    pass


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    m = float(len(hand))

    total = float(sum(hand))

    return float(total/m)

    pass


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    actual_avg = sum(hand) / len(hand)

    # middle value (for odd-length list)
    middle_value = hand[len(hand) // 2]

    # average of first and last
    first_last_avg = (hand[0] + hand[-1]) / 2

    return actual_avg == middle_value or actual_avg == first_last_avg

def average_even_is_average_odd(hand):
    even = []
    odd = []

    for i in range(len(hand)):
        if i % 2 == 0:      
            even.append(hand[i])
        else:               
            odd.append(hand[i])

    avg_even = float(sum(even) / len(even))
    avg_odd = float(sum(odd) / len(odd))

    return avg_even == avg_odd
    


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    jack = 11

    if hand[-1] == jack:
        hand[-1] = hand[-1]*2

    return hand
