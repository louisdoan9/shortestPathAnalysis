import random
import matplotlib.pyplot as plot
import numpy as np
from Dijkstra import dijkstra, dijkstra_approx
from Bellman_ford import bellman_ford, bellman_ford_approx
from random_graph import create_random_complete_graph, create_random_graph
from total_distance import total_dist

# experiment code for observing the difference between both approximations and their original versions
# when the maximum number of relaxations allowed changes
list1 = [i for i in range(101)]
list2 = []
list3 = []

for k in range(101):
    g = create_random_complete_graph(50, 50)
    j = random.randint(0, 49)
    list2.append(total_dist(dijkstra_approx(g, j, k)) - total_dist(dijkstra(g, j)))
    list3.append(total_dist(bellman_ford_approx(g, j, k)) - total_dist(bellman_ford(g, j)))

plot.plot(list1, list2, label="dijkstra")
plot.plot(list1, list3, label="bellman-ford")
plot.title("the difference between the approximations and their original versions when the maximum number of relaxations allowed changes")
plot.xlabel('number of relaxations allowed')
plot.ylabel('difference')
plot.legend()
plot.xticks(np.arange(10, 101, 10))
plot.show()