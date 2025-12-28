def resistor_label(colors):
    code = {
        'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
        'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
    }

    multiplier = {
        'black': 1,
        'brown': 10,
        'red': 100,
        'orange': 1_000,
        'yellow': 10_000,
        'green': 100_000,
        'blue': 1_000_000,
        'violet': 10_000_000,
        'grey': 100_000_000,
        'white': 1_000_000_000,
        'gold': 0.1,
        'silver': 0.01
    }

    tolerance = {
        'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%',
        'green': '0.5%', 'brown': '1%', 'red': '2%',
        'gold': '5%', 'silver': '10%'
    }

    # Special case: 1-band resistor
    if len(colors) == 1:
        return "0 ohms"

    # 4-band resistor
    if len(colors) == 4:
        base = code[colors[0]] * 10 + code[colors[1]]
        value = base * multiplier[colors[2]]
        tol = tolerance[colors[3]]

    # 5-band resistor
    elif len(colors) == 5:
        base = code[colors[0]] * 100 + code[colors[1]] * 10 + code[colors[2]]
        value = base * multiplier[colors[3]]
        tol = tolerance[colors[4]]

    # Format output
    if value < 1_000:
        out = f"{int(value)} ohms"
    elif value < 1_000_000:
        out = f"{value/1000:g} kiloohms"
    elif value < 1_000_000_000:
        out = f"{value/1_000_000:g} megaohms"
    else:
        out = f"{value/1_000_000_000:g} gigaohms"

    return f"{out} ±{tol}"
