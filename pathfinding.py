from collections import deque

def dfs(graph, start, goal):
    stack = [start]
    visited = set()
    path = []
    while stack:
        vertex = stack.pop()
        if vertex in visited:
            continue
        visited.add(vertex)
        path.append(vertex)
        if vertex == goal:
            return path
        for neighbor in reversed(list(graph.neighbors(vertex))):
            if neighbor not in visited:
                stack.append(neighbor)
    return None

# slightly broken at the moment
def bfs(graph, start, goal):
    queue = deque([start])  # Use deque for efficient append and pop from the left
    visited = set()
    path = []
    parent = {start: None}  # Track the path

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        if current == goal:
            break
        for neighbor in graph.neighbors(current):
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
                parent[neighbor] = current  # Keep track of parents to reconstruct the path

    # Reconstruct the path from goal to start using the parent dictionary
    step = goal
    while step is not None:
        path.append(step)
        step = parent.get(step)

    return path[::-1]  # Return reversed path