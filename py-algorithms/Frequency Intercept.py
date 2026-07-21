def analyze_comms(comms_log,target):
    if not isinstance(comms_log,tuple):
        return "Error invalid"
    if not isinstance(target,str):
        return "Error invalid"
    
    count_var = comms_log.count(target)
    if count_var == 0:
        return "Target frequency empty."
    
    index_var = target.index(target)

    sorted_list = sorted(comms_log, reverse=True)

    return f"Target {target} detected {count_var} times. First contact at index {index_var}. Archive: {sorted_list}"