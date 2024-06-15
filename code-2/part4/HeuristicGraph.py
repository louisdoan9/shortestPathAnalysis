from WeightedGraph import WeightedGraph

class HeuristicGraph(WeightedGraph):
    
    def __init__(self, heuristic):
        self.heuristic = heuristic

    def get_heuristic(self):
        return self.heuristic