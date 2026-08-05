# The Scenario:
# The Syndicate has a list of bounties on rival hackers. 
# You need to process the ledger to see who was actually captured, 
# filter out the low-level bounties, take the Syndicate's 20% tax from the payouts, and calculate your net profit.

def process_bounties(targets,captured,bounties):
    if not isinstance(targets,list) or not isinstance(captured,list) or not isinstance(bounties,list):
        return "Error: Something went wrong"

    secured_bounties = []
    for target,status,bounty in zip(targets,captured,bounties):
        if status == True:
            secured_bounties.append((target,bounty))

    elite_bounties = list(filter(lambda x:x[1] > 10000, secured_bounties))


    final_cuts = [int(num[1] * 0.80) for num in elite_bounties]

    vault_total =sum(final_cuts)

    return {"elite_targets_caught": len (elite_bounties), "net_profit": vault_total}