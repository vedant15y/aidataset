# Practical 2: IMPLEMENTING BFS AND DFS

Objective: To represent a graph in Python and implement Breadth-First Search (BFS) and Depth-First Search (DFS) traversal algorithms.
Scenario: A delivery company models its city hub network as a graph, where each node is a hub and each edge is a direct road connection. The dispatch team wants to find a path from the Central Hub to a destination hub.

## Question 1: Graph Representation using Adjacency List

### Question 1 - Adjacency List Definition

```python
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
```

### Sample output from the source report

```text
Central -> ['North', 'West']
North -> ['Central', 'NorthEast', 'East']
West -> ['Central', 'SouthWest']
NorthEast -> ['North']
East -> ['North', 'SouthEast']
SouthWest -> ['West']
SouthEast -> ['East']
```

## Question 2: Breadth-First Search (BFS) Implementation

### Question 2 - BFS Queue Traversal

```python
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
```

### Sample output from the source report

```text
BFS traversal order: ['Central', 'North', 'West', 'NorthEast', 'East', 'SouthWest', 'SouthEast']
```

## Question 3: Depth-First Search (DFS) Implementation

### Question 3 - Recursive DFS Traversal

```python
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
```

### Sample output from the source report

```text
DFS traversal order: ['Central', 'North', 'NorthEast', 'East', 'SouthEast', 'West', 'SouthWest']
```

## Question 4: Shortest Path Finding with BFS (Central to SouthEast)

### Question 4 - BFS Shortest Path Code

```python
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
```

### Sample output from the source report

```text
Path from Central to SouthEast: Central -> North -> East -> SouthEast
```

## Question 5: Algorithmic Comparison of BFS vs. DFS

| Evaluation Aspect | Breadth-First Search (BFS) | Depth-First Search (DFS) |
| --- | --- | --- |
| Traversal Style | Level-by-level (breadth-first) | Goes deep along one branch first |
| Data Structure | FIFO Queue (collections.deque) | LIFO Stack / Function Call Stack (Recursion) |
| Shortest Path (Unweighted) | Guarantees fewest edge transitions | Does not guarantee shortest path |
| Primary Use Case | Nearest hub routing, shortest delivery path | Exploring all reachable nodes, cycle detection, topological sorting |
| Memory Footprint | O(b^d) - stores all nodes at active level | O(b * m) - generally lower memory for deep graphs |
