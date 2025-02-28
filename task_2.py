"""
This module implements DFS and BFS algorithms for finding paths in a graph.
It applies these algorithms to the transport network graph and compares their results.
"""

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Створюємо граф транспортної мережі (як у Task 1)
G = nx.Graph()
edges = [
    ("Kyiv", "Lviv"), ("Kyiv", "Odesa"), ("Kyiv", "Kharkiv"), ("Kyiv", "Dnipro"),
    ("Lviv", "Odesa"), ("Lviv", "Kharkiv"), ("Odesa", "Dnipro"), ("Kharkiv", "Dnipro")
]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
plt.title("Transport Network Graph")
plt.show()

# Алгоритм DFS (Пошук у Глибину)
def dfs(graph, start, goal):
    stack = [(start, [start])]  # Стек для збереження поточного шляху
    paths = []
    
    while stack:
        vertex, path = stack.pop()
        for neighbor in set(graph[vertex]) - set(path):  # Уникнення циклів
            new_path = path + [neighbor]
            if neighbor == goal:
                paths.append(new_path)
            else:
                stack.append((neighbor, new_path))
    
    return paths

# Алгоритм BFS (Пошук у Ширину)
def bfs(graph, start, goal):
    queue = deque([(start, [start])])  # Використовуємо deque для оптимізації
    paths = []
    
    while queue:
        vertex, path = queue.popleft()
        for neighbor in set(graph[vertex]) - set(path):  # Уникнення циклів
            new_path = path + [neighbor]
            if neighbor == goal:
                paths.append(new_path)
            else:
                queue.append((neighbor, new_path))
    
    return paths

# Вибір стартової та цільової вершини
start_node = "Kyiv"
goal_node = "Dnipro"

# Виконання DFS та BFS
dfs_paths = dfs(G, start_node, goal_node)
bfs_paths = bfs(G, start_node, goal_node)

# Вивід результатів
print(f"🔍 DFS-шляхи від {start_node} до {goal_node}:")
for path in dfs_paths:
    print(" → ".join(path))

print(f"\n🔍 BFS-шляхи від {start_node} до {goal_node}:")
for path in bfs_paths:
    print(" → ".join(path))

# Пояснення різниці між DFS та BFS
print("\n📌 Порівняння DFS і BFS:")
print("✔ DFS (пошук у глибину) рухається вниз по одній гілці графа до кінця, перш ніж повертатися назад.")
print("✔ BFS (пошук у ширину) проходить всі сусідні вершини перш, ніж заглиблюватись, тому завжди знаходить найкоротший шлях за кількістю кроків.")
