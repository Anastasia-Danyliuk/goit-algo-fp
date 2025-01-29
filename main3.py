import heapq
import networkx as nx


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor in graph.neighbors(current_vertex):
            weight = graph[current_vertex][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


G = nx.Graph()
nodes = ["Сільпо", "АТБ", "Фора", "Аврора", "НП", "Розетка", "Зал", "Метро"]
G.add_nodes_from(nodes)
edges = [
    ("Сільпо", "АТБ", 5),
    ("Сільпо", "Фора", 10),
    ("Сільпо", "НП", 7),
    ("АТБ", "Фора", 3),
    ("АТБ", "Аврора", 8),
    ("АТБ", "Розетка", 6),
    ("Фора", "Аврора", 2),
    ("Фора", "Зал", 4),
    ("Аврора", "Метро", 5),
    ("НП", "Розетка", 2),
    ("НП", "Метро", 8),
    ("Розетка", "Зал", 3),
    ("Зал", "Метро", 1)
]
G.add_weighted_edges_from(edges)

print(dijkstra(G, 'Сільпо'))
