def intercepted_data(raw_manifest,is_authorized,price_per_part,discount_code):
    if not isinstance(raw_manifest,str):
        return "Error in parts"
    raw_manifest =raw_manifest.strip().split('-')
    parts_count = len(raw_manifest)
    clean_manifest = " ".join(raw_manifest)

    if is_authorized == False:
        return "Error: Unauthorized mechanic"
    if not isinstance(price_per_part,(int,float)):
        return "Error: Price should be Integer or Float"
    
    total_cost = parts_count * price_per_part

    if discount_code == "CREW_VIP":
        total_cost = total_cost - (total_cost * 0.2)

    return f"Order: {clean_manifest} | Parts: {parts_count} | Total: ${total_cost}"