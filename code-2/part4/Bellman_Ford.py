from SPAlgorithm import SPAlgorithm

class Bellman_Ford(SPAlgorithm):

    def calc_sp(G, source, dest):
        pred = {}
        dist = {}
        nodes = list(G.adj.keys())

        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        for _ in range(G.get_num_of_nodes()):
            for node in nodes:
                for neighbour in G.adj[node]:
                    if dist[neighbour] > dist[node] + G.w(node, neighbour):
                        dist[neighbour] = dist[node] + G.w(node, neighbour)
                        pred[neighbour] = node
        return dist[dest]