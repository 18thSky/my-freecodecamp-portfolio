def battle(our_team, opponent):
    our_list = our_team.split(" ")
    their_list = opponent.split(" ")
    team_score = 0

    for our_word,their_word in zip(our_list,their_list):
        our_power  = 0
        for letter in our_word:
            letter_val = ord(letter.lower()) - 96
            if letter.isupper():
                letter_val = letter_val * 2
            our_power += letter_val

        their_power  = 0
        for letter in their_word:
            letter_val = ord(letter.lower()) - 96
            if letter.isupper():
                letter_val = letter_val * 2
            their_power += letter_val
        if our_power > their_power:
            team_score += 1
        if their_power > our_power:
            team_score -= 1
    if team_score > 0:
        return "We win"
    elif team_score < 0:
        return "We lose"
    else:
        return "Draw"