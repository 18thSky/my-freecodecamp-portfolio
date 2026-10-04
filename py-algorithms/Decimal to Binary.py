def to_binary(decimal):
    if not isinstance(decimal,int):
        return "Number should be postive"
    if decimal == 0:
            return "0"
    binary_result = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_result = str(remainder) + binary_result
        decimal = decimal // 2
        
    return binary_result
