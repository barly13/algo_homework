def dfs(graph, v, parent, visited):
    visited[v] = True

    for el in graph[v]:
        if el != parent:
            if el in visited or dfs(graph, el, v, visited):
                return True

    return False


def has_cycle(graph):
    visited = [False] * len(graph)

    for i in range(len(graph)):
        if not visited[i]:
            if dfs(graph, i, None, visited):
                return True

    return False