def value(colors):
    code = {
        "black": '0',
        "brown": '1',
        "red": '2',
        "orange": '3',
        "yellow": '4',
        "green": '5',
        "blue": '6',
        "violet": '7',
        "grey": '8',
        "white": '9'
    }

    color = list(colors)

    return int(code[color[0]] + code[color[1]])
