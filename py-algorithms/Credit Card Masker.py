def mask(card):
    hidden_part = card[:-4]
    visible_part = card[-4:]
    masked_string = ""
    for char in hidden_part:
        if char.isdigit():
            masked_string += "*"
        else:
            masked_string += char
    return masked_string + visible_part