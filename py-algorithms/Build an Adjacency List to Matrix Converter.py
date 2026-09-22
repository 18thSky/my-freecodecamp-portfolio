def adjacency_list_to_matrix(adjacency_list):
    # Find the number of nodes in the graph
    node_no = len(adjacency_list)

    # Create an empty matrix with node_no rows and node_no columns
    matrix = []
    for _ in range(node_no):
        matrix.append([0] * node_no)

    # Go through every node and its neighbors
    # Mark 1 where an edge exists
    for node in adjacency_list:
        for neighbor in adjacency_list[node]:
            matrix[node][neighbor] = 1

    # Print each row of the adjacency matrix
    for row in matrix:
        print(row)

    # Return the completed adjacency matrix
    return matrix
