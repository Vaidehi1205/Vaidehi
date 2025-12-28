def proteins(strand):
    codon_to_amino = {
        "AUG": "Methionine",

        "UUU": "Phenylalanine", "UUC": "Phenylalanine",
        "UUA": "Leucine",       "UUG": "Leucine",

        "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",

        "UAU": "Tyrosine", "UAC": "Tyrosine",

        "UGU": "Cysteine", "UGC": "Cysteine",

        "UGG": "Tryptophan",

        "UAA": "STOP", "UAG": "STOP", "UGA": "STOP"
    }

    result = []

    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]

        if codon in ("UAA", "UAG", "UGA"):
            break

        if codon in codon_to_amino:
            result.append(codon_to_amino[codon])

    return result
