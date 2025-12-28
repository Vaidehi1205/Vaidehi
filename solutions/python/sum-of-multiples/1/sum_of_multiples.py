def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    
    for n in range(1, limit):
        if any(n % m == 0 for m in multiples if m != 0):
            unique_multiples.add(n)
            
    return sum(unique_multiples)

