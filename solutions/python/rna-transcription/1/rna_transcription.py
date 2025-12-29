def to_rna(dna_strand):
    co = list(dna_strand)

    for i in range(len(co)):
        if co[i] == 'A':
            co[i] = 'U'
        elif co[i] == 'C':
            co[i] = 'G'
        elif co[i] == 'G':
            co[i] = 'C'
        elif co[i] == 'T':
            co[i] = 'A'

    return ''.join(co)