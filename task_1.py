"""
This module performs graph analysis using the networkx library.
It creates and manipulates graphs for various use cases, including PageRank and shortest path algorithms.
"""

import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()

# Додаємо вершини (міста)
cities = ["Kyiv", "Lviv", "Odesa", "Kharkiv", "Dnipro"]
G.add_nodes_from(cities)

# Додаємо ребра (маршрути між містами) з відстанями
edges = [
    ("Kyiv", "Lviv", 540),
    ("Kyiv", "Odesa", 475),
    ("Kyiv", "Kharkiv", 480),
    ("Kyiv", "Dnipro", 420),
    ("Lviv", "Odesa", 700),
    ("Lviv", "Kharkiv", 1000),
    ("Odesa", "Dnipro", 550),
    ("Kharkiv", "Dnipro", 210)
]

# Додаємо ребра до графа з вагою
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Візуалізація графа
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Transport Network Graph")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_sequence = [G.degree(n) for n in G.nodes()]

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступені вершин:", degree_sequence)
