import networkx as nx


def build_digraph_with_weights():
    """
    Read data from the standard input and build the corresponding
    directed graph with weights. Nodes numbering starts with number
    1 (that is, nodes are 1,2,3,...)
    """

    graph = nx.DiGraph()
    graph_list = []

    with open('./dataset/graph_1.txt', 'r') as f:
        first_line = f.readline().split()
        for x in range(1, int(first_line[0])):
            graph.add_node(x)

        for line in f:
            divided = line.split()
            graph_list.append([int(divided[0]), int(divided[1]), {'weight': int(divided[2])}])

    graph.add_edges_from(graph_list)

    return graph
"""
    first_line = input().split()
    num_nodes = int(first_line[0])
    num_edges = int(first_line[1])

    # Crear grafo direcional con num_nodes

    # Añadir los vértices del grafo

    return graph
"""