from datetime import date
def moon_phase(date_string):
    target_date = date.fromisoformat(date_string)
    reference = date.fromisoformat("2000-01-06")
    time_delta = target_date - reference
    days_passed = time_delta.days
    lunar_cycle = (days_passed % 28)+1
    if lunar_cycle <=7:
        return "New"
    elif lunar_cycle <=14 and lunar_cycle >7:
        return "Waxing"
    elif lunar_cycle <=21 and lunar_cycle > 14:
        return "Full"
    elif lunar_cycle <=28 and lunar_cycle>21:
        return"Waning"
