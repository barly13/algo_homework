def is_bipartite(graph):
    colors = [0] * len(graph)

    def dfs(node, color):
        colors[node] = color

        for neighbor in graph[node]:
            if colors[neighbor] == 0:
                if not dfs(neighbor, -color):
                    return False

            elif colors[neighbor] == colors[node]:
                return False

        return True

    for i in range(len(graph)):
        if colors[i] == 0:
            if not dfs(i, 1):
                return False

    return True