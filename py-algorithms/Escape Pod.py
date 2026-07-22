def override_timer(start_time):
    if not isinstance(start_time,int):
        return "Error invalid input"
    
    launch_log = []

    for num in range(start_time,0,-1):
        launch_log.append(num)

    launch_log.append("IGNITION")
    
    return launch_log