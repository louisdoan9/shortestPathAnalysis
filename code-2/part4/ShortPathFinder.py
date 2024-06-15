class ShortPathFinder:

    def __init__(self):
        self.graph = None
        self.algorithm = None

    def calc_short_path(self, source, dest):
        return self.algorithm.calc_sp(self.graph, source, dest)
    
    def set_graph(self, graph):
        self.graph = graph
    
    def set_algorithm(self, algorithm):
        self.algorithm = algorithm