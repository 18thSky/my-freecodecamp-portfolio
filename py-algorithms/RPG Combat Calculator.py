def calculate_damage(attack,defense,is_critical):
    if not isinstance(attack,(int,float)):
        return 'Error: Invalid data types'
    elif not isinstance(defense,(int,float)):
        return 'Error: Invalid data types'
    elif not isinstance(is_critical,bool):
        return 'Error: Invalid data types'
    
    raw_damage = attack - defense

    if is_critical == True:
        raw_damage *= 2

    if raw_damage < 0:
        raw_damage = 0

    final_damage = int(raw_damage)

    if is_critical == True:
        return f"Critical hit! You dealt {final_damage} damage."
    else:
        return f"You dealt {final_damage} damage."