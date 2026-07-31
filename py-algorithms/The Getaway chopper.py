# The Scenario:
# The chopper has a strict weight limit, but you need to maximize your profit. 
# You have three data streams detailing the loot. You need to sync them, 
# filter out the heavy items, calculate your total payout, 
# and send the final manifest to the pilot.

def load_chopper(manifest, weights,values):

    if not isinstance(manifest,list) or not isinstance(weights,list) or not isinstance(values,list):
        return "Error: something went wrong"

    secured_loot =[]

    for item_manifest,item_weights,item_values in zip(manifest,weights,values):
        if item_weights < 60:
            secured_loot.append((item_manifest, item_values))

    payouts = [item[1] for item in secured_loot]

    total_payout = sum(payouts)

    return {"items_secured": len(secured_loot), "total_value": total_payout}