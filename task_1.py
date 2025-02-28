"""
This module analyzes a transport network graph of major Ukrainian cities using NetworkX.
It visualizes the network and calculates key metrics such as degree distribution, 
shortest paths, and graph density.
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
G.add_weighted_edges_from(edges)

# Візуалізація графа
pos = nx.kamada_kawai_layout(G)  # Використовуємо більш природний розклад
labels = nx.get_edge_attributes(G, 'weight')

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Transport Network Graph")
plt.show()

# Аналіз характеристик графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_sequence = [G.degree(n) for n in G.nodes()]
avg_degree = sum(degree_sequence) / num_nodes
density = nx.density(G)

# Найкоротші шляхи між деякими містами
shortest_paths = {
    (city1, city2): nx.shortest_path_length(G, city1, city2, weight='weight')
    for city1 in cities for city2 in cities if city1 != city2
}

# Виведення характеристик графа
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Середній ступінь вершини: {avg_degree:.2f}")
print(f"Щільність графа: {density:.4f}")
print("Ступені вершин:", degree_sequence)

# Вивід декількох прикладів найкоротших шляхів
print("\nПриклади найкоротших шляхів за відстанню:")
for (city1, city2), dist in list(shortest_paths.items())[:5]:  # Показати 5 прикладів
    print(f"{city1} → {city2}: {dist} км")
