"""Practical 2: IMPLEMENTING BFS AND DFS.

Extracted from BSBXLB302P_AI_Lab_Practical_Report.docx.
"""

# Graph representation using an adjacency list (dict of lists)
graph = {
    "Central": ["North", "West"],
    "North": ["Central", "NorthEast", "East"],
    "West": ["Central", "SouthWest"],
    "NorthEast": ["North"],
    "East": ["North", "SouthEast"],
    "SouthWest": ["West"],
    "SouthEast": ["East"]
}

for node, neighbors in graph.items():
    print(f"{node} -> {neighbors}")

from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

bfs_order = bfs(graph, "Central")
print("BFS traversal order:", bfs_order)

def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []
    
    visited.add(start)
    order.append(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order

dfs_order = dfs(graph, "Central")
print("DFS traversal order:", dfs_order)

from collections import deque

def bfs_path(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None

path = bfs_path(graph, "Central", "SouthEast")
print("Path from Central to SouthEast:", " -> ".join(path))
