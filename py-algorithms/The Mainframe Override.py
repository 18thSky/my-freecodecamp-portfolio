# The Scenario:
# You bypassed the keypad and reached the Syndicate's mainframe. 
# The data is heavily encrypted and split into three separate data streams. 
# You must sync the streams, filter out the dangerous security nodes, extract the heavy data packets, 
# and find the even-numbered bypass codes.

def override_mainframe(security_logs,threat_levels,raw_data):
    if not isinstance(security_logs,list) or not isinstance(threat_levels,list) or not isinstance(raw_data,list):
        return "Error: Something wend wrong"
    
    safe_nodes = []

    for log,threat in zip(security_logs,threat_levels):
        if threat < 5:
            safe_nodes.append(log)

    heavy_packets = list(filter(lambda x: x > 100,raw_data))

    total_data = sum(heavy_packets)

    even_codes = [num for num in raw_data if num % 2 == 0]

    return {"safe": safe_nodes, "data": total_data, "codes": even_codes}