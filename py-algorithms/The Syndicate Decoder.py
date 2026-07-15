def decode_transmission(encrypted_location,base_price,hazard_level,is_night_race,override_key):
    if not isinstance(encrypted_location,str):
        return "Error: Invalid transmission"
    if not isinstance(override_key,str):
        return "Error: Invalid transmission"
    if not isinstance(base_price,(int,float)):
        return "Error: Invalid transmission"
    if not isinstance(hazard_level,int):
        return "Error: Invalid transmission"
    if not isinstance(is_night_race,bool):
        return "Error: Invalid transmission"
    if is_night_race == True and override_key == "":
        return "Access Denied: Night races require an override key."
    
    # This does all your cleaning in one single, beautiful line of code:
    encrypted_location = encrypted_location.strip(" <>").replace("-", "").replace("_", " ").upper()
    # encrypted_location = encrypted_location.strip()
    # encrypted_location = encrypted_location.replace('-',"")
    # encrypted_location = encrypted_location.replace('_',"")
    # encrypted_location = encrypted_location.upper()

    total_price = base_price * hazard_level
    if is_night_race == True:
        total_price  += 500.0
    
    syndicate_cut = total_price//2
    syndicate_cut= int(syndicate_cut)

    return f"Race at {encrypted_location}. Payout: ${syndicate_cut}"