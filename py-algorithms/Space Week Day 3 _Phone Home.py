def send_message(route):
    time_travel = sum(route)/300000
    delay_time = (len(route) - 1) * 0.5
    number = time_travel + delay_time
    return round(number,4)