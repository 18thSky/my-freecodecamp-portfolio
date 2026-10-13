def hex_to_decimal(hex):
    total = 0
    power = 0
    hex_chars = "0123456789ABCDEF"
    for char in reversed(hex):
        number = hex_chars.index(char)
        total += number * (16 ** power)
        power += 1
    return total