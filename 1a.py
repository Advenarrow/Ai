import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# 1. Define the Graph (Exactly as per your record)
graph = {
    0: [1, 3],
    1: [0, 2],
    2: [0, 4],
    3: [],
    4: [3]
}

# 2. BFS Traversal Function
def bfs(graph, start):
    visited = []             # Fixed syntax error from PDF
    queue = deque([start])
    order = []
    visited.append(start)

    while queue:
        node = queue.popleft()
        order.append(node)
        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
                
    print("BFS traversal:", *order)

# 3. Graph Drawing Code
def draw_graph(graph):
    G = nx.DiGraph() # Directed Graph
    for node in graph:
        for neighbor in graph[node]:
            G.add_edge(node, neighbor)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2000)
    plt.title("BFS Graph Representation")
    plt.show()

# Run both
bfs(graph, 0)
draw_graph(graph)