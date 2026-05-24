def transpose(text):
    if text == "":
        return ""

    lines = text.split("\n")
    max_len = max(len(line) for line in lines)

    result = []

    for col in range(max_len):
        row = ""

        for r in range(len(lines)):
            if col < len(lines[r]):
                row += lines[r][col]
            else:
                if any(col < len(lines[k]) for k in range(r + 1, len(lines))):
                    row += " "

        result.append(row)

    return "\n".join(result)