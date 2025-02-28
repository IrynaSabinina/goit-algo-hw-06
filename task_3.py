"""
This module performs graph analysis using the networkx library.
It creates and manipulates graphs for various use cases, including PageRank and shortest path algorithms.
""" 

import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()
edges = [
    ('A', 'B', 1), ('A', 'C', 4), 
    ('B', 'D', 2), ('B', 'E', 5), 
    ('C', 'F', 3), ('D', 'G', 1), 
    ('E', 'H', 2), ('F', 'I', 3)
]
G.add_weighted_edges_from(edges)

# Візуалізація графа з вагами
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_color='black')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Граф з вагами")
plt.show()

# Алгоритм Дейкстри
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    visited = set()
    
    while len(visited) < len(graph.nodes):
        # Вибір вузла з найменшою відстанню
        current_node = min((node for node in graph.nodes if node not in visited), key=lambda node: distances[node])
        visited.add(current_node)
        
        for neighbor in graph[current_node]:
            weight = graph[current_node][neighbor]['weight']
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight
                
    return distances

# Знайдемо найкоротші шляхи від стартової вершини 'A'
start_node = 'A'
shortest_paths = dijkstra(G, start_node)

# Вивід результатів
print(f"Найкоротші відстані від вершини '{start_node}':")
for node, distance in shortest_paths.items():
    print(f"Відстань до '{node}': {distance}")