def process_vault(vault_record,crew_list):
    if not isinstance(vault_record,tuple) or not isinstance(crew_list,list):
        return "Error: Invalid"
    
    vault_id,total_cash, *loot = vault_record
    active_members = crew_list

    if ("Data Drive") not in loot:
        return "Mission Failed: Primary target missing."
    
    loot.sort()
    payout = int(total_cash) // len(crew_list)

    return f"Vault {vault_id} secured. Payout per crew: ${payout}. Loot: {loot}"