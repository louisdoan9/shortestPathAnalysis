import a_star
import shortest_path

G_numberphile = shortest_path.DirectedWeightedGraph(13)

nodes = ["S", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
for node in nodes:
    G_numberphile.add_node(node)

G_numberphile.add_edge("S", "A", 7)
G_numberphile.add_edge("A", "S", 7)

G_numberphile.add_edge("S", "B", 2)
G_numberphile.add_edge("B", "S", 2)

G_numberphile.add_edge("S", "C", 3)
G_numberphile.add_edge("C", "S", 3)

G_numberphile.add_edge("A", "B", 3)
G_numberphile.add_edge("B", "A", 3)

G_numberphile.add_edge("A", "D", 4)
G_numberphile.add_edge("D", "A", 4)

G_numberphile.add_edge("B", "D", 4)
G_numberphile.add_edge("D", "B", 4)

G_numberphile.add_edge("B", "H", 1)
G_numberphile.add_edge("H", "B", 1)

G_numberphile.add_edge("C", "L", 2)
G_numberphile.add_edge("L", "C", 2)

G_numberphile.add_edge("D", "F", 5)
G_numberphile.add_edge("F", "D", 5)

G_numberphile.add_edge("H", "F", 3)
G_numberphile.add_edge("F", "H", 3)

G_numberphile.add_edge("H", "G", 2)
G_numberphile.add_edge("G", "H", 2)

G_numberphile.add_edge("L", "I", 4)
G_numberphile.add_edge("I", "L", 4)

G_numberphile.add_edge("L", "J", 4)
G_numberphile.add_edge("J", "L", 4)

G_numberphile.add_edge("I", "J", 7)
G_numberphile.add_edge("J", "I", 7)

G_numberphile.add_edge("I", "K", 4)
G_numberphile.add_edge("K", "I", 4)

G_numberphile.add_edge("J", "K", 4)
G_numberphile.add_edge("K", "J", 4)

G_numberphile.add_edge("K", "E", 5)
G_numberphile.add_edge("E", "K", 5)

G_numberphile.add_edge("G", "E", 2)
G_numberphile.add_edge("E", "G", 2)

def heuristic(node):
    numberphile_heur = {"S": 10, "A": 9, "B": 7, "C": 8, "D": 7, "E": 0, "F": 6, "G": 3, "H": 6, "I": 4, "J": 4, "K": 3, "L": 6}
    return numberphile_heur[node]

print(a_star.a_star(G_numberphile, "S", "E", heuristic))
