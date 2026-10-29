"""Practical 3: IMPLEMENTING A* SEARCH.

Extracted from BSBXLB302P_AI_Lab_Practical_Report.docx.
"""

# Grid definition: 0 = Open Cell, 1 = Shelving Obstacle
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Charging dock
goal = (4, 4)   # Target picking location
print("Start:", start, "| Goal:", goal)

def manhattan(a, b):
    # h(n) = |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

h_estimate = manhattan(start, goal)
print("Heuristic estimate from start to goal:", h_estimate)

import heapq

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    # Priority Queue stores tuples: (f_score, g_score, current_node, path_taken)
    open_set = [(manhattan(start, goal), 0, start, [start])]
    visited = set()
    
    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        
        if current == goal:
            return path, g
            
        if current in visited:
            continue
        visited.add(current)
        
        r, c = current
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        for nr, nc in neighbors:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    new_g = g + 1
                    new_f = new_g + manhattan((nr, nc), goal)
                    heapq.heappush(open_set, (new_f, new_g, (nr, nc), path + [(nr, nc)]))
                    
    return None, float("inf")

path, cost = a_star(grid, start, goal)
print("Optimal path:", path)
print("Path cost:", cost)

def print_grid_with_path(grid, path):
    display = [[str(cell) for cell in row] for row in grid]
    for r, c in path:
        if (r, c) == start:
            display[r][c] = "S"
        elif (r, c) == goal:
            display[r][c] = "G"
        else:
            display[r][c] = "*"
            
    for row in display:
        print("  ".join(row))

print(f"Optimal path found with cost = {cost} steps:\n")
print_grid_with_path(grid, path)
