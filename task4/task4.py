import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        # Унікальний ідентифікатор для кожного вузла
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()

# Функція для перетворення списку в бінарну купу (мін-купа)
def build_min_heap(elements):
    heapq.heapify(elements)
    return elements

# Функція для побудови дерева з бінарної купи
def build_tree_from_heap(heap):
    nodes = [Node(key) for key in heap]
    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0] if nodes else None

def main():
    # Створення та візуалізація бінарної купи
    elements = [3, 1, 6, 5, 2, 8, 7]
    min_heap = build_min_heap(elements)
    print("Min-heap:", min_heap)
    heap_tree_root = build_tree_from_heap(min_heap)

    # Відображення дерева бінарної купи
    draw_tree(heap_tree_root)


if __name__ == "__main__":
    main()
