# The Scenario:
# The Syndicate just pulled off two massive simultaneous jobs (Job Alpha and Job Beta). 
# You need to find the elite operatives who worked both jobs, 
# check their clearance levels in the master database, and calculate their final payout based on a base rate. 
# If a rogue hacker isn't in the database, they get the standard base rate (multiplier of 1.0).

# 1. Master function calculate_payouts and below 4 will be its parameters
# 2. Two database which can hold 2 crew_database(dictionary) which will be job_alpha_team and job_beta_team which will be a list
# 3. And integer named base_payout to get cash pile
# 4. Will need to create a variable named elite_hackers which will hold hackers who did job in both teams using Intersection Operator job_alpha_team & job_beta_team
# 5. final_roster new empty variable
# 5. A for loop to check each hacker in new elite_hacker variable
# 6. multiplier = crew_database.get(hacker, 1.0) for DB query
# 7. base_payout by multiplier found in DB query and it should return number
# 8. final_roster[hacker] = calculated_payout since we need to add only one hacker to rooster just use bracket notation
# 9. return final_roster

def calculate_payouts(crew_databases,job_alpha_team,job_beta_team,base_payout):
    if not isinstance(crew_databases,dict) or not isinstance(job_alpha_team,set) or not isinstance(job_beta_team,set) or not isinstance(base_payout,int):
        return "Error: Something went wrong"

    elite_hackers = job_beta_team & job_alpha_team

    final_roster = {}

    for hacker in elite_hackers:
        multiplier = crew_databases.get(hacker, 1.0)

        payout = int(base_payout * multiplier)

        final_roster[hacker] = payout

    return final_roster