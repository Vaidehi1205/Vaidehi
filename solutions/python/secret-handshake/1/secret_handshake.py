def commands(binary_str):
    bin = list(binary_str)

    handShake = []

    if bin[-1] == '1':
        handShake.append('wink')
    if bin[-2] == '1':
        handShake.append('double blink')
    if bin[-3] == '1':
        handShake.append('close your eyes')
    if bin[-4] == '1':
        handShake.append('jump')

    if bin[0] == '1':
        handShake.reverse()
        return handShake
    else:
        return handShake
     
