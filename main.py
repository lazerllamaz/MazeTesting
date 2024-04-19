import sys
from maze_config import maze
from graph_tools import create_maze_graph, find_special_points
from pathfinding import bfs, dfs
from visualization import draw_maze_graph
#from genetic_algorithm import ga

''' Run using python main.py bfs|dfs '''
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [bfs|dfs]")
        sys.exit(1)

    method = sys.argv[1].lower()
    if method not in ['bfs', 'dfs']:
        print("Invalid method. Choose 'bfs' or 'dfs'.")
        sys.exit(1)

    G = create_maze_graph(maze)
    start = find_special_points(maze, 2)
    goal = find_special_points(maze, 3)

    if start is None or goal is None:
        print("Error: Start point '2' or goal point '3' not defined in the maze.")
        sys.exit(1)

    if method == 'bfs':
        path = bfs(G, start, goal)
        print("Using BFS. Path from start to goal:", path)
    elif method == 'dfs':
        path = dfs(G, start, goal)
        print("Using DFS. Path from start to goal:", path)

    draw_maze_graph(G, maze, path)