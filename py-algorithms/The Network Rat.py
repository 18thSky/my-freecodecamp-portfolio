# The Scenario:
# You have a dump of the server logs. The logs are a "nested list" (a list containing smaller lists). 
# Each smaller list represents a specific server, and contains the usernames of everyone who accessed it. 
# You need to track exactly which servers a suspicious user accessed, and how many times they pinged it.

def scan_servers(server_logs,suspect):
    if not isinstance(server_logs,list) or not isinstance(suspect,str):
        return "Error something went wrong"

    rat_activity = {}
    for server_id, user_list in enumerate(server_logs):
        if suspect in user_list:
            suspect_count = user_list.count(suspect)
            rat_activity[server_id] = suspect_count

    return rat_activity