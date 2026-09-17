def verify_card_number(card_number):
    double = False
    total = 0
    card_number = card_number.replace("-", "")
    card_number = card_number.replace(" ", "")

    for digit in reversed(card_number):
        print(digit)
        digit = int(digit)

        if double:
            digit = int(digit)
            digit = digit * 2
            

        if digit > 9:
            
            digit = digit - 9
        
        total += digit

        if double == True:
            double = False
        else:
            double = True

    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"