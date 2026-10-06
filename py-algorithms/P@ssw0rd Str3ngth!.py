def check_strength(password):
    score = 0
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False
    if len(password) >= 8:
        score += 1
    
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_number = True
        if char in "!@#$%^&*":
            has_special = True
    if has_upper and has_lower:
        score += 1
    if has_number:
        score +=1
    if has_special:
        score +=1

    if score == 4:
        return "strong"
    elif score >= 2:
        return "medium"
    else:
        return "weak"
        