# The Scenario:
# You pulled off the heist, but the cash is dirty. 
# You need to process it through the Syndicate's offshore accounts. 
# However, some accounts are flagged by the feds, and the Syndicate takes a flat fee for every deposit.

def launder_cash(account_status,deposits):
    if not isinstance(account_status,list) or not isinstance(deposits,list):
        return "Error:Something went wrong"

    clean_deposits=[]

    for status, amount in zip(account_status,deposits):
        if status == "Clean":
            clean_deposits.append(amount)

    heavy_deposits = list(filter(lambda x:x >200, clean_deposits))

    final_cut = list(map(lambda x:x -100, heavy_deposits))

    vault_total = sum(final_cut)

    return {"clean": clean_deposits, "taxed": final_cut, "total": vault_total}