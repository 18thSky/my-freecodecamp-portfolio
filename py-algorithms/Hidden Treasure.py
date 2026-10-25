def dive(map, coordinates):
    row = coordinates[0]
    column = coordinates[1]
    target_cell = map[row][column]
    zero_count = 0
    for current_row in map:
        for cell in current_row:
            if cell == target_cell:
                zero_count += 1
    if target_cell == "-":
        return "Empty"
    elif zero_count > 1:
        return "Found"
    elif zero_count == 1:
        return "Recovered"


dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 1]) 

dive([[ "-", "X"], [ "-", "X"], [ "-", "O"]], [2, 0])

dive([[ "-", "X"], [ "-", "O"], [ "-", "O"]], [1, 1])

dive([[ "-", "-", "-"], [ "X", "O", "X"], [ "-", "-", "-"]], [1, 2])

dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [2, 0])

dive([[ "-", "-", "-"], [ "-", "-", "-"], [ "O", "X", "X"]], [1, 2])