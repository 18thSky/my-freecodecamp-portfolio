def number_pattern(n):
    if not isinstance(n,int):
            return 'Argument must be an integer value.'
    if n <= 0:
            return 'Argument must be an integer greater than 0.'

    result = []
    for number in range(1,n+1):
        result.append(str(number))
    return " ".join(result)