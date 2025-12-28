def distance(strand_a, strand_b):
    count = 0

    A = list(strand_a)
    B = list(strand_b)

    if len(A) != len(B):
        raise ValueError("Strands must be of equal length.")
    else:
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1

    return count