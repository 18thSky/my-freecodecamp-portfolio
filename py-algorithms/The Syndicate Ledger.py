def process_ledger(crew_accounts,loot_cache,syndicate_tax):
    if not isinstance(crew_accounts,dict):
        return "Error: Corrupted Ledger"
    if not isinstance(loot_cache,list):
        return "Error: Corrupted Ledger"
    if not isinstance(syndicate_tax,int):
        return "Error: Corrupted Ledger"

    high_value_loot = [item for item in loot_cache if item[1]>=1000]
    total_value = sum([item[1] for item in high_value_loot])

    final_cut = int(total_value -(total_value * (syndicate_tax/100)))
    payout = int(final_cut // len(crew_accounts))

    for member in crew_accounts:
        crew_accounts[member] += payout

    return crew_accounts