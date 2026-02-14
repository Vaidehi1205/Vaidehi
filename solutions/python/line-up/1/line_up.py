def line_up(name, number):
    num = str(number)
    if num.endswith("1") and "11" not in num:
        return f"{name}, you are the {number}st customer we serve today. Thank you!"
    elif num.endswith("2") and "12" not in num:
        return f"{name}, you are the {number}nd customer we serve today. Thank you!"
    elif num.endswith("3") and "13" not in num:
        return f"{name}, you are the {number}rd customer we serve today. Thank you!"
    else:
        return f"{name}, you are the {number}th customer we serve today. Thank you!"
