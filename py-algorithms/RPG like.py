def calculate_damage(attack,defense,is_critical):
    if not isinstance(attack,(int,float)):
        return 'Error: Invalid data types'
    elif not isinstance(defense,(int,float)):
        return 'Error: Invalid data types'
    elif not isinstance(is_critical,bool):
        return 'Error: Invalid data types'
    
    final_damage = raw_damage(defense - attack)
    if is_critical == True:
        return 
        raw_damage *= 2
    elif defense < 0:
        return 
        final_damage = 0