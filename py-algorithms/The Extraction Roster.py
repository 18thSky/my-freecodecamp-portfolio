def secure_extraction(active_crew,backups,kia_member):
    if not isinstance(active_crew,list) or not isinstance(backups,list):
        return "Error"
    if not isinstance(kia_member,str):
        return "Error"
    
    if kia_member in active_crew:
        active_crew.remove(kia_member)
    
    active_crew.extend(backups)

    active_crew.insert(0,"The Boss")

    active_crew.sort()

    passenger_count = len(active_crew)

    return f"Chopper inbound for {passenger_count} targets. Manifest:{active_crew}"