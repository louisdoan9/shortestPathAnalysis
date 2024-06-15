from SPAlgorithm import SPAlgorithm
from HeuristicGraph import HeuristicGraph
import min_heap

class A_star_helper(SPAlgorithm):

    def calc_sp(G, source, dest, h):
        pred = {}
        dist = {}
        Q = min_heap.MinHeap([])
        nodes = list(G.adj.keys())

        for node in nodes:
            Q.insert(min_heap.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, h[source])

        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value

            if current_node == dest:
                break

            dist[current_node] = current_element.key - h[current_node]

            for neighbour in G.get_adj_nodes(current_node):
                if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour) + h[neighbour])
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    pred[neighbour] = current_node

        path = [dest]
        while path[-1] != source:
            path.append(pred[path[-1]])
        path.reverse()

        return dist[dest]
