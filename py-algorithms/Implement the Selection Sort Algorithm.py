def selection_sort(list_of_items):
    for i in range(len(list_of_items)):
        minimum_index = i

        for j in range(i + 1, len(list_of_items)):
            if list_of_items[j] < list_of_items[minimum_index]:
                minimum_index = j
        
        if minimum_index != i:
            list_of_items[i],list_of_items[minimum_index] =list_of_items[minimum_index], list_of_items[i]
    return list_of_items
