import matplotlib.pyplot as plt
import networkx as nx

def draw_maze_graph(G, maze, path=None):
    # Create positions for all nodes based on their (row, column) locations
    pos = {(r, c): (c, -r) for r in range(len(maze)) for c in range(len(maze[0])) if maze[r][c] != 1}
    # Draw the graph using the positions
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')
    
    if path:
        # Make sure the path is not None and all nodes in the path have a position
        if all(node in pos for node in path):
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
        else:
            print("Error: One or more nodes in the path do not have positions.")
    plt.show()
