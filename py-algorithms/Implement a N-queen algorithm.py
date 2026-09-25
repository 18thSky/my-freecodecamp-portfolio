def dfs_n_queens(n):
    list_of_solutions = []

    if not isinstance(n, int):
        return 'Should be a number'

    if n < 1:
        return []

    queens = []

    def backtrack():
        # We placed a queen in every row
        if len(queens) == n:
            list_of_solutions.append(queens.copy())
            return

        # Try every column in the current row
        for column in range(n):

            # Column is already occupied
            if column in queens:
                continue

            conflict = False

            # Check this position against every existing queen
            for index, existing_column in enumerate(queens):

                # Same diagonal
                if abs(len(queens) - index) == abs(column - existing_column):
                    conflict = True
                    break

            # This position isn't safe
            if conflict:
                continue

            # Place the queen
            queens.append(column)

            # Move to the next row
            backtrack()

            # Undo the choice and try another column
            queens.pop()

    backtrack()

    return list_of_solutions


print(dfs_n_queens(1))
print(dfs_n_queens(4))
print(len(dfs_n_queens(8)))
