# visualization.py
import networkx as nx
import matplotlib.pyplot as plt

def visualize_grid(graph, title="Smart Grid Power Flow Network"):
    """
    Visualizes the directed graph with edge capacities.
    """
    G = nx.DiGraph()
    for u in graph:
        for v, cap in graph[u].items():
            G.add_edge(u, v, capacity=cap)

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', arrows=True)
    labels = nx.get_edge_attributes(G, 'capacity')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.title(title)
    plt.show()
