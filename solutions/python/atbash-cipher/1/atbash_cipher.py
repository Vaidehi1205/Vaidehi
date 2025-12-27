def encode(plain_text):
    clean_text = "".join(c.lower() for c in plain_text if c.isalnum())
    
    encoded_list = []
    for char in clean_text:
        if char.isalpha():
            encoded_list.append(chr(219 - ord(char)))
        else:
            encoded_list.append(char)
            
    full_cipher = "".join(encoded_list)
    
    return " ".join(full_cipher[i:i + 5] for i in range(0, len(full_cipher), 5))

        

def decode(ciphered_text):
    clean_text = ciphered_text.replace(" ", "")
    
    decoded_list = []
    for char in clean_text:
        if char.isalpha():
            decoded_list.append(chr(219 - ord(char)))
        else:
            decoded_list.append(char)
            
    return "".join(decoded_list)

