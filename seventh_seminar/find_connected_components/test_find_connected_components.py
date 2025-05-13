from typing import Dict, List


def find_connected_components(graph: Dict[int, List[int]]) -> Dict[int, int]:
    visited = {}

    def dfs(v: int, color: int):
        visited[v] = color

        for neighbor in graph[v]:
            if visited[neighbor] == 0:
                dfs(neighbor, color)

    for i in range(len(graph)):
        visited[i] = 0

    color = 0
    for node in graph:
        if visited[node] == 0:
            color += 1
            dfs(node, color)

    return visited
