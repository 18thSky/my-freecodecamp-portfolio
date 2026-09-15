def quick_sort(list_of_integers):
    if len(list_of_integers) < 2:
        return list_of_integers
    pivot = list_of_integers[0]
    less = []
    equal = []
    greater = []

    for number in list_of_integers:
        if number < pivot:
            less.append(number)
        elif number == pivot:
            equal.append(number)
        else:
            greater.append(number)
    return quick_sort(less) + equal + quick_sort(greater)

    