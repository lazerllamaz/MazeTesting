import networkx as nx

def find_special_points(maze, value):
    for r, row in enumerate(maze):
        for c, val in enumerate(row):
            if val == value:
                return (r, c)
    return None

def create_maze_graph(maze):
    rows, cols = len(maze), len(maze[0])
    Maze = nx.Graph()
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != 1:  # Assume 1 is a wall, ignore walls
                node = (r, c)
                if r > 0 and maze[r-1][c] != 1:
                    Maze.add_edge(node, (r-1, c))
                if r < rows-1 and maze[r+1][c] != 1:
                    Maze.add_edge(node, (r+1, c))
                if c > 0 and maze[r][c-1] != 1:
                    Maze.add_edge(node, (r, c-1))
                if c < cols-1 and maze[r][c+1] != 1:
                    Maze.add_edge(node, (r, c+1))
    return Maze
