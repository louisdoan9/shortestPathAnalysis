from A_star import A_star
from WeightedGraph import WeightedGraph
from ShortPathFinder import ShortPathFinder

SPF = ShortPathFinder()
SPF.set_algorithm(A_star())
SPF.set_graph(WeightedGraph())

result = SPF.calc_short_path(0, 2)

print(result)