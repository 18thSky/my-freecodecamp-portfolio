def analyze_bounty(target_data,active_zone):
    if not isinstance(target_data,list):
        return "Error: Invalid data" 
    if not isinstance(active_zone,str):
        return "Error: Invalid data"
    
    target_name, hazard_multiplier, locations, is_armed = target_data

    if active_zone not in locations:
        return "Target lost. Outside active zone."
    sliced_list = locations[0:2]
    final_amount = 10000 * hazard_multiplier
    if is_armed == True:
        final_amount += 5000
    final_amount = int(final_amount)

    return f"Bounty: {target_name}. Primary zones: {sliced_list}. Payout: ${final_amount}"