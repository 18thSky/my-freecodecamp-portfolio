def crack_keypad(data_stream):
    if not isinstance(data_stream,list):
        return "Error"
    
    secret_word = ""
    total_count = 0
    
    for item in data_stream:
        if isinstance(item,str):
            secret_word += item
        elif isinstance(item,int):
            total_count += item

    return {"keyword": secret_word, "access_code": total_count}