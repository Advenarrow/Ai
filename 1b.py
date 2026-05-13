import networkx as nx
import matplotlib.pyplot as plt

# 1. Define the Graph
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2, 4],
    4: [3]
}

# 2. DFS Traversal Function (Corrected Recursion)
def dfs(graph, start, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []

    visited.add(start)
    order.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    
    return order

# 3. Graph Drawing Code
def draw_dfs_graph(graph):
    G = nx.Graph() # Undirected Graph as per your record
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)
            
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=2000)
    plt.title("DFS Graph Representation")
    plt.show()

# Run both
traversal = dfs(graph, 0)
print("DFS Traversal:", *traversal)
draw_dfs_graph(graph)