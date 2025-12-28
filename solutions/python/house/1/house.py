def recite(start_verse, end_verse):
    ry = [
    ("malt", "lay in"),
    ("rat", "ate"),
    ("cat", "killed"),
    ("dog", "worried"),
    ("cow with the crumpled horn", "tossed"),
    ("maiden all forlorn", "milked"),
    ("man all tattered and torn", "kissed"),
    ("priest all shaven and shorn", "married"),
    ("rooster that crowed in the morn", "woke"),
    ("farmer sowing his corn", "kept"),
    ("horse and the hound and the horn", "belonged to"),
    ]

    ins = ["the %s that %s " % (x, y) for x, y in ry]

    verses = []

    for n in range(start_verse, end_verse + 1):
        part = "".join(ins[:n-1][::-1])
        verse = "This is " + part + "the house that Jack built."
        verses.append(verse)

    return verses
