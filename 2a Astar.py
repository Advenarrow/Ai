import matplotlib.pyplot as plt 
import networkx as nx 

# Corrected Graph Dictionary
graph = {
    'A': [('B', 1), ('D', 3)], 
    'B': [('A', 1), ('C', 3), ('D', 4)], 
    'C': [('B', 2), ('D', 5), ('E', 2)], 
    'D': [('A', 3), ('B', 4), ('C', 5), ('E', 3)], 
    'E': [('C', 2), ('D', 3)]
} 

# Heuristic values h(n)
heuristic = { 
    'A': 4, 'B': 3, 'C': 1, 'D': 10, 'E': 0 
} 

def a_star(start, goal): 
    # open_list stores (f_cost, g_cost, current_node)
    open_list = [(heuristic[start], 0, start)] 
    visited = set() 
    traversal = [] 
    
    while open_list: 
        open_list.sort() # Sort by f_cost
        f, g, node = open_list.pop(0) 
        
        if node not in traversal:
            traversal.append(node) 
            
        if node == goal: 
            print("\nGoal reached!") 
            return traversal 
            
        visited.add(node) 
        for child, cost in graph[node]: 
            if child not in visited: 
                g_new = g + cost 
                f_new = g_new + heuristic[child] 
                open_list.append((f_new, g_new, child)) 
    return traversal 

# Execution
path = a_star('A', 'E') 
print("Traversal order:", path) 

# -------- Graph Drawing -------- 
G = nx.Graph() 
for node, neighbors in graph.items(): 
    for neighbor, weight in neighbors: 
        G.add_edge(node, neighbor, weight=weight) 

pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500) 
edge_labels = nx.get_edge_attributes(G, 'weight') 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) 

# Highlight the traversal path in red
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=1500)
plt.title("A* Search Path (Nodes in Red)") 
plt.show()