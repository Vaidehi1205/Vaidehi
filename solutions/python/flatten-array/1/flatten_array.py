def flatten(iterable):
    A = []

    for item in iterable:
        if isinstance(item, list):
            A.extend(flatten(item))
        elif item is not None:
            A.append(item)

    return A
