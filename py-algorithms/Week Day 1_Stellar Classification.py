def classification(temp):
    if temp == "":
        return "Value is empty"
    elif temp < 0:
        return "Value needs to be higher than zero"
    elif temp <= 3699:
        return "M"
    elif temp <= 5199:   # Automatically knows it's >= 3700!
        return "K"
    elif temp <= 5999:   # Automatically knows it's >= 5200!
        return "G"
    elif temp <= 7499:
        return "F"
    elif temp <= 9999:
        return "A"
    elif temp <= 29999:
        return "B"
    else: 
        return "O"