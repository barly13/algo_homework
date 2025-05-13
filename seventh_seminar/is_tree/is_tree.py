def is_tree(graph, start):
    visited = []
    queue = [start]
    parent = {start: None}

    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)
                parent[neighbour] = vertex

            else:
                if parent[neighbour] == neighbour:
                    return False

    return len(visited) == len(graph)