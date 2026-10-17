def validate(email):
    if email.count("@") != 1:
        return False

    local,domain = email.split("@")
    if ".." in local or ".." in domain:
        return False
        
    if local.startswith(".") or local.endswith("."):
        return False
    
    for char in local:
        if not char.isalnum() and char not in "._-":
            return False
    if "." not in domain:
        return False
    parts = domain.split(".")
    # parts[-1]
    if len(parts[-1]) < 2 or not parts[-1].isalpha():
        return False
    return True