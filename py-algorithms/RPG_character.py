full_dot = '●'
empty_dot = '○'


def create_character(character_name,character_strength,character_intelligence,character_charisma): 
    # Create a functiom and pass the parameters

    if not isinstance(character_name,(str)):
        return 'The character name should be a string'
    # if not string return
    elif len(character_name) == 0:
        return 'The character should have a name'
    # The character should have a name
    elif len(character_name) > 10:
        return 'The character name is too long'
    # Name is more than 10 words
    elif " " in character_name:
        return 'The character name should not contain spaces'
    # No empty spaces

    if not isinstance(character_strength,(int)) or not isinstance(character_intelligence,(int)) or not isinstance(character_charisma,(int)):
        return 'All stats should be integers'
    elif (character_strength < 1) or (character_intelligence < 1) or (character_charisma < 1):
        return 'All stats should be no less than 1'
    elif (character_strength > 4) or (character_intelligence > 4) or (character_charisma > 4):
        return 'All stats should be no more than 4'
    elif (character_strength + character_intelligence + character_charisma) != 7:
        return 'The character should start with 7 points'
    
    str_line = "STR " + (full_dot * character_strength) + (empty_dot * (10 - character_strength))

    int_line = "INT " + (full_dot * character_intelligence) + (empty_dot * (10 - character_intelligence))

    cha_line = "CHA " + (full_dot * character_charisma) + (empty_dot * (10 - character_charisma))

    return f"{character_name}\n{str_line}\n{int_line}\n{cha_line}" 