from SPAlgorithm import SPAlgorithm
from HeuristicGraph import HeuristicGraph
from A_star_helper import A_star_helper
import min_heap

class A_star(SPAlgorithm):

    def calc_sp(G, source, dest):
        h = {}

        if not isinstance(G, HeuristicGraph):
            for node in range(G.get_num_of_nodes()):
                h[node] = 0
        else:
            h = G.get_heuristic()

        return A_star_helper.calc_sp(G, source, dest, h)