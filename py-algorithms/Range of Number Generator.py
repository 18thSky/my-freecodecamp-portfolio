def range_of_numbers(start_num,end_num):
    if start_num == end_num:
        return [start_num]
        
    elif not start_num <= end_num:
        print('Invalid operation')
    elif start_num <= end_num:
        result = range_of_numbers(start_num + 1,end_num)
        result.insert(0,start_num)
        return result