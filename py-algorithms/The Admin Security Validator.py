def is_valid_admin(password):
    if not isinstance(password,str):
        return 'Error: Must be text'
    elif len(password) < 10:
        return False
    elif not password.startswith('ADMIN_'):
        return False
    elif " " in password:
        return False
    else:
        return True