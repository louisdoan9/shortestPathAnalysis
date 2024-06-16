import random
import matplotlib.pyplot as plot
import numpy as np
from Dijkstra import dijkstra, dijkstra_approx
from Bellman_ford import bellman_ford, bellman_ford_approx
from random_graph import create_random_complete_graph, create_random_graph
from total_distance import total_dist

"""
Experiment 1

For both Dijkstra's and Bellman Ford's shortest path algorithm, compare the difference
in distance between each algorithms corresponding approximation version to the original.

Compare the relationship of the above when the number of nodes, number of edges,
number of relaxations change.
"""

# experiment code for observing the difference between both approximations and their original versions
# when the density of the graphs change

list1 = [i for i in range(50, 101)]
list2 = []
list3 = []
for i in range(50, 101):
    g = create_random_graph(50, i, 10)
    j = 0
    k = 20
    r = random.randint(0, 49)
    while dijkstra_approx(g, 0, k)[r] == float("inf"):
        r = random.randint(0, 49)
    list2.append(dijkstra_approx(g, 0, k)[r] - dijkstra(g, 0)[r])
    while bellman_ford_approx(g, 0, k)[r] == 0:
        r = random.randint(0, 49)
    list3.append(bellman_ford_approx(g, 0, k)[r] - bellman_ford(g, 0)[r])
plot.plot(list1, list2, label="dijkstra")
plot.plot(list1, list3, label="bellman-ford")
plot.title("the difference between the approximations and their original versions when the density of the graph changes")
plot.xlabel('number of edges')
plot.ylabel('difference')
plot.legend()
plot.xticks(np.arange(50, 101, 10))
plot.show()


# experiment code for observing the difference between both approximations and their original versions
# when the size of the graphs change
list1 = [i for i in range(10, 101)]
list2 = []
list3 = []
for i in range(10, 101):
    g = create_random_complete_graph(i, i)
    j = random.randint(0, i - 1)
    k = 20
    list2.append(total_dist(dijkstra_approx(g, j, k)) - total_dist(dijkstra(g, j)))
    list3.append(total_dist(bellman_ford_approx(g, j, k)) - total_dist(bellman_ford(g, j)))
plot.plot(list1, list2, label="dijkstra")
plot.plot(list1, list3, label="bellman-ford")
plot.title("the difference between the approximations and their original versions when the number of nodes in the complete graph changes")
plot.xlabel('number of nodes')
plot.ylabel('difference')
plot.legend()
plot.xticks(np.arange(10, 101, 10))
plot.show()

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