def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    div = []

    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    else:
        for i in range(1,number):
            if number % i == 0:
                div.append(i)

        if number == (sum(div)):
            return "perfect"
        elif number < sum(div):
            return "abundant"
        elif number > sum(div):
            return "deficient"
    
    
    