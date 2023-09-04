"""
Doramitzi Esmeralda Herrera Zepeda
20310343
"""

from collections import deque

def bfs(graph, start):
    visited = set()  # conjunto de nodos visitados
    queue = deque([start])  # cola de nodos por visitar

    while queue:
        node = queue.popleft()  # obtenemos el siguiente nodo a visitar
        if node not in visited:
            visited.add(node)  # lo añadimos al conjunto de nodos visitados
            print(node)  # imprimimos el nodo visitado

            # agregamos a la cola los vecinos del nodo actual
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Ejemplo de uso
graph = {
    'A': ['B', 'C', 'G'],
    'B': ['A', 'D', 'G'],
    'C': ['A', 'D', 'E'],
    'D': ['C', 'B', 'F'],
    'E': ['C', 'G', 'F'],
    'F': ['E', 'D', 'H'],
    'G': ['A', 'B', 'E'],
    'H': ['F']
}

bfs(graph, 'C')
