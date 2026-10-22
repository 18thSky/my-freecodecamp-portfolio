def adjust_thermostat(current_f, target_c):
    target_f = (target_c * 1.8) + 32
    
    if current_f == target_f:
        return "Hold"
    if current_f < target_f:
        difference = target_f - current_f
        return f"Heat: {difference:.1f} degrees Fahrenheit"
    if current_f > target_f:
        difference = current_f - target_f
        return f"Cool: {difference:.1f} degrees Fahrenheit"
    