def find_landing_spot(matrix):
    lowest_danger = float('inf')
    best_spot = []
    for row in range(len(matrix)):
        for column in range (len(matrix[row])):
            current_cell = matrix[row][column]
            if current_cell ==0:
                current_danger = 0
                if row > 0:
                    current_danger += matrix[row-1][column]
                if row < len(matrix) - 1:
                    current_danger += matrix[row+1][column]
                if column > 0:
                    current_danger += matrix[row][column-1] 
                if column < len(matrix[row]) -1:
                    current_danger += matrix[row][column+1]
                if current_danger < lowest_danger:
                    lowest_danger = current_danger
                    best_spot = [row,column]

    return best_spot