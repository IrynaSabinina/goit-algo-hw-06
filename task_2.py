"""
This module performs graph analysis using the networkx library.
It creates and manipulates graphs for various use cases, including PageRank and shortest path algorithms.
"""

import networkx as nx
import matplotlib.pyplot as plt

# Створюємо граф
G = nx.Graph()
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), 
    ('B', 'E'), ('C', 'F'), ('D', 'G'), 
    ('E', 'H'), ('F', 'I')
]
G.add_edges_from(edges)

# Візуалізація графа
nx.draw(G, with_labels=True, node_color='lightblue', node_size=800, font_size=10, font_color='black')
plt.title("Граф")
plt.show()

# Алгоритм DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Алгоритм BFS
def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Виконання алгоритмів
start_node = 'A'
goal_node = 'H'

dfs_paths = list(dfs(G, start_node, goal_node))
bfs_paths = list(bfs(G, start_node, goal_node))

# Вивід результатів
print("Шляхи, знайдені за допомогою DFS:")
for path in dfs_paths:
    print(path)

print("\nШляхи, знайдені за допомогою BFS:")
for path in bfs_paths:
    print(path)

# Пояснення
print("\nПояснення:")
print("DFS (пошук в глибину) зазвичай знаходить шлях, проходячи до найглибших вузлів перед поверненням. Це може призводити до довгих шляхів.")
print("BFS (пошук в ширину) знаходить найкоротший шлях в термінах кількості ребер, оскільки досліджує всі сусіди на поточному рівні перед переходом на наступний.")