# The Scenario:
# The Syndicate just finished a massive week of operations. 
# You have a messy list of the crew members, a list of the hours they worked, 
# and a secure database of their hourly rates. You need to calculate everyone's pay, 
# format a clean audit log for the boss, and calculate the total amount of cash leaving the vault.

"""
1. Create a master function called audit_payroll with parameters
2. Crew(members) and hours(hours worked) which are list and a dict called rate_db(members:hour worked)
3. Add isinstance check for all 3 parameters if follow the type which we passing or else return an error
4. Need to create 2 variables a. total_vault_cash which is a int and set to 0 
5. An empty List audit_log
6. using a For loop and zip()method we need to iterate through every crew and hours entries at same time
7. Create a new variable to save .lower text of hackers to clean_name
8. Using Get list method we need to look up name from rate_db list and if its not present in DB return 100
9. To Calculate payout we need to do math, hacker's hours * rate = total_vault_cash
10. we need to return a formatted string return f""{hacker_name}.capitalize()": "{rate}""
11. Also we need to add  get this some how {"total_paid": total_vault_cash, "log": audit_log}

"""
def audit_payroll(crew,hours,rate_db):
    if not isinstance(crew,list) or not isinstance(hours,list) or not isinstance(rate_db,dict):
        return "Error: Something went wrong"

    total_vault_cash = 0
    audit_log = []

    for hacker_name,hour in zip(crew,hours):
        clean_name = hacker_name.lower()

        rate = rate_db.get(clean_name, 100)
        payout = hour * rate
        total_vault_cash += payout
        audit_log.append(f"{clean_name.capitalize()}: ${payout}")

    return {"total_paid": total_vault_cash, "log": audit_log}

