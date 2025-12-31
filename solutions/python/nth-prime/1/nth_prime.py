def prime(number):
    if number <= 0:
        raise ValueError("there is no zeroth prime")

    primes = []
    candidate = 2

    while len(primes) < number:
        is_prime = True
        for i in range(2, int(candidate ** 0.5) + 1):
            if candidate % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(candidate)

        candidate += 1

    return primes[number - 1]
