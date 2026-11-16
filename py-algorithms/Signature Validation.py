def verify(message, key, signature):
    def get_char_value(char):
        if 'a' <= char <= 'z':
            lower_case = ord(char)-96
            return lower_case
        if 'A' <= char <= 'Z':
            upper_case = ord(char) - 38
            return upper_case
        else:
            return 0
    total_sum = 0
    for char in message:
        total_sum += get_char_value(char)
    for keys in key:
        total_sum += get_char_value(keys)
    if total_sum == signature:
        return True
    else:
        return False