def launch_fuel(payload):
    
    total_fuel = payload/5
    total_mass = total_fuel + payload
    additional_fuel = total_fuel

    while additional_fuel >=1:
        new_fuel = total_mass/5
        additional_fuel = new_fuel - total_fuel 
        total_fuel = new_fuel
        total_mass = payload + total_fuel
    return round(total_fuel, 1)