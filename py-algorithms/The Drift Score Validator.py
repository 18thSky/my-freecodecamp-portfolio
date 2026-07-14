def validate_drift(player,base_score,multiplier,is_cheating):
    if not isinstance(player,str):
        return "Error: Invalid run data"
    if not isinstance(base_score,(int,float)):
        return "Error: Invalid run data"
    if not isinstance(multiplier,(int,float)):
        return "Error: Invalid run data"
    if not isinstance(is_cheating,bool):
        return "Error: Invalid run data"
    if is_cheating == True:
        return "Disqualified"
    if base_score == 0 or multiplier == 0:
        return False
    
    final_score = base_score * multiplier
    final_score = int(final_score)
    return f"{player} scored {final_score} points!"
