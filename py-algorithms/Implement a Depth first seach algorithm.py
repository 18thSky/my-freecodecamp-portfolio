def dfs(undirected_matrix,start_node):
    visited = []
    stack = [start_node]
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.append(current_node)
            for neighbor,is_connected in enumerate(undirected_matrix[current_node]):
                if is_connected == 1 and neighbor not in visited:
                    stack.append(neighbor)
    return visited