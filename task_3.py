"""
This module implements Dijkstra's algorithm to find the shortest paths in a weighted transport network graph.
It calculates the shortest paths between all cities and visualizes the graph.
"""

import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Створюємо граф транспортної мережі з вагами (відстані в км)
G = nx.Graph()
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
G.add_weighted_edges_from(edges)

# Візуалізація графа з вагами
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G, seed=42)  # Фіксуємо розташування вершин
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Transport Network with Weights")
plt.show()

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    """Знаходить найкоротші шляхи від стартової вершини до всіх інших у графі."""
    distances = {node: float('inf') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0
    pq = [(0, start)]  # Пріоритетна черга (вага, вузол)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        for neighbor in graph[current_node]:
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:  # Оновлюємо відстань
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes

# Функція для відновлення найкоротшого шляху
def reconstruct_path(previous_nodes, start, end):
    """Відновлює найкоротший шлях між двома вершинами."""
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    return path[::-1]  # Реверсуємо шлях

# Обчислення найкоротших шляхів від кожної вершини
shortest_paths_all = {}
for city in G.nodes:
    distances, previous_nodes = dijkstra(G, city)
    shortest_paths_all[city] = (distances, previous_nodes)

# Вивід результатів
for start_city, (distances, previous_nodes) in shortest_paths_all.items():
    print(f"\n🚏 Найкоротші шляхи від {start_city}:")
    for target_city in G.nodes:
        if target_city != start_city:
            path = reconstruct_path(previous_nodes, start_city, target_city)
            print(f"{start_city} → {target_city}: {distances[target_city]} км, шлях: {' → '.join(path)}")
