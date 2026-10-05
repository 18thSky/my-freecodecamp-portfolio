def to_decimal(binary):
    reversed_string = binary[::-1]
    total_sum = 0
    tracker = 0
    power = 0
    while tracker < len(reversed_string):
        current_digit = reversed_string[tracker]
        total_sum += int(current_digit) * (2 ** power)
        tracker += 1
        power += 1
    return total_sum