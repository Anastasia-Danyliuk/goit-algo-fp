from collections import deque
import uuid
import networkx as nx
import matplotlib.pyplot as plt

def generate_color(index, total):
    intensity = int(255 * (index / total))
    return f"#{intensity:02x}{intensity:02x}FF"

def bfs_iterative_visual(graph, start):
    visited = set()
    queue = deque([start])
    colors = {}
    step = 0

    while queue:
        vertex = queue.popleft()
        if vertex.id not in visited:
            print(vertex.val, end=" ")
            visited.add(vertex.id)
            colors[vertex.id] = generate_color(step, len(graph))
            step += 1

            for neighbor in graph[vertex]:
                if neighbor.id not in visited:
                    queue.append(neighbor)

    return colors

def dfs_iterative_visual(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    colors = {}
    step = 0

    while stack:
        vertex = stack.pop()
        if vertex.id not in visited:
            print(vertex.val, end=' ')
            visited.add(vertex.id)
            colors[vertex.id] = generate_color(step, len(graph))  # Генеруємо колір
            step += 1
            stack.extend(reversed(graph[vertex]))

    return colors

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if colors:
        for node_id, color in colors.items():
            tree.nodes[node_id]['color'] = color

    node_colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

def build_graph(node, graph=None):
    if graph is None:
        graph = {}
    if node is not None:
        if node not in graph:
            graph[node] = []
        if node.left:
            graph[node].append(node.left)
            build_graph(node.left, graph)
        if node.right:
            graph[node].append(node.right)
            build_graph(node.right, graph)
    return graph

graph = build_graph(root)

print("BFS обхід:")
bfs_colors = bfs_iterative_visual(graph, root)
draw_tree(root, bfs_colors)

print("\nDFS обхід:")
dfs_colors = dfs_iterative_visual(graph, root)
draw_tree(root, dfs_colors)