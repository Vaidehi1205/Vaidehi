def label(colors):
    color_map = [
        'black', 'brown', 'red', 'orange', 'yellow',
        'green', 'blue', 'violet', 'grey', 'white'
    ]
    
    prefixes = {
        0: "ohms",
        1: "kiloohms",
        2: "megaohms",
        3: "gigaohms",
    }

    try:
        digit1 = color_map.index(colors[0].lower())
        digit2 = color_map.index(colors[1].lower())
        significant_value = (digit1 * 10) + digit2
        
        multiplier_power = color_map.index(colors[2].lower())

        total_ohms = significant_value * (10 ** multiplier_power)

        value_to_display = float(total_ohms)
        prefix_index = 0
        
        while value_to_display >= 1000 and prefix_index < len(prefixes) - 1:
            value_to_display /= 1000
            prefix_index += 1
            
        format_string = "{:.1f}".format(value_to_display).rstrip('0').rstrip('.')
        
        return f"{format_string} {prefixes[prefix_index]}"

    except (ValueError, IndexError):
        return "Error: Invalid color name or insufficient colors provided."

