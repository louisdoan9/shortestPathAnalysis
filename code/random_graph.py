from DirectedWeightedGraph import DirectedWeightedGraph
import random

def create_random_complete_graph(n, upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i, j, random.randint(1, upper))
    return G

def create_random_graph(n, upper, e):
    G = DirectedWeightedGraph()
    count = 0
    for i in range(n):
        G.add_node(i)
        if i != 0:
            G.add_edge(0, i, random.randint(1, upper))
        G.add_edge(i, i, 0)
    while count < e:
        i = random.randint(1, n-1)
        j = random.randint(1, n-1)
        if i != j:
            G.add_edge(i, j, random.randint(1, upper))
        count += 1
    return G