import min_heap
import random
import matplotlib.pyplot as plot
import timeit
import numpy as np


class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)


def dijkstra(G, source):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist


def bellman_ford(G, source):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    nodes = list(G.adj.keys())

    # Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    # Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist


def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total


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


# Assumes G represents its nodes as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d


def init_d(G):
    n = G.number_of_nodes()
    d = [[float("inf") for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i, j):
                d[i][j] = G.w(i, j)
        d[i][i] = 0
    return d


def dijkstra_approx(G, source, k):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    counter = 0
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)
    # Meat of the algorithm
    # for node in nodes:
    #     if node == source:
    #         dist[node] = 0
    #     else:
    #         dist[node] = G.w(source, node)
    while not Q.is_empty():
        counter = 0
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour] and counter < k:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
                counter += 1
    return dist


def bellman_ford_approx(G, source, k):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    nodes = list(G.adj.keys())
    count = {}

    # Initialize distances
    for node in nodes:
        dist[node] = float("inf")
        count[node] = 0
    dist[source] = 0

    # Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and count[neighbour] < k:
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
                    count[neighbour] += 1
    return dist


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


# experiment code for observing the difference between both approximations and their original versions
# when the density of the graphs change
# list1 = [i for i in range(50, 101)]
# list2 = []
# list3 = []
# for i in range(50, 101):
#     g = create_random_graph(50, i, 10)
#     j = 0
#     k = 20
#     r = random.randint(0, 49)
#     while dijkstra_approx(g, 0, k)[r] == float("inf"):
#         r = random.randint(0, 49)
#     list2.append(dijkstra_approx(g, 0, k)[r] - dijkstra(g, 0)[r])
#     while bellman_ford_approx(g, 0, k)[r] == 0:
#         r = random.randint(0, 49)
#     list3.append(bellman_ford_approx(g, 0, k)[r] - bellman_ford(g, 0)[r])
# plot.plot(list1, list2, label="dijkstra")
# plot.plot(list1, list3, label="bellman-ford")
# plot.title("the difference between the approximations and their original versions when the density of the graph changes")
# plot.xlabel('number of edges')
# plot.ylabel('difference')
# plot.legend()
# plot.xticks(np.arange(50, 101, 10))
# plot.show()


# experiment code for observing the difference between both approximations and their original versions
# when the size of the graphs change
# list1 = [i for i in range(10, 101)]
# list2 = []
# list3 = []
# for i in range(10, 101):
#     g = create_random_complete_graph(i, i)
#     j = random.randint(0, i - 1)
#     k = 20
#     list2.append(total_dist(dijkstra_approx(g, j, k)) - total_dist(dijkstra(g, j)))
#     list3.append(total_dist(bellman_ford_approx(g, j, k)) - total_dist(bellman_ford(g, j)))
# plot.plot(list1, list2, label="dijkstra")
# plot.plot(list1, list3, label="bellman-ford")
# plot.title("the difference between the approximations and their original versions when the number of nodes in the complete graph changes")
# plot.xlabel('number of nodes')
# plot.ylabel('difference')
# plot.legend()
# plot.xticks(np.arange(10, 101, 10))
# plot.show()


# experiment code for comparing the output of mystery to dijkstra
# when all weights are positive
# for i in range(100):
#     g = create_random_complete_graph(5, 5)
#     print(mystery(g))
#     for j in range(g.number_of_nodes()):
#         print(dijkstra(g, j))

# experiment code for comparing the output of mystery to dijkstra
# graphs include negative weights
# for i in range(10):
#     g = create_random_complete_graph(3, 3)
#     for k in range(3):
#         i = random.randint(0, 2)
#         j = random.randint(0, 2)
#         if i != j:
#             g.weights[(i, j)] = random.randint(-2, -1)
#     print(g.weights)
#     print(mystery(g))
# note: running the following produces an error
#     for j in range(g.number_of_nodes()):
#         print(dijkstra(g, j))


# experiment to determine run time complexity of mystery function
# list1 = [i for i in range(1, 151)]
# list2 = []
# for i in range(1, 151):
#     g = create_random_complete_graph(i, i)
#     start = timeit.default_timer()
#     mystery(g)
#     end = timeit.default_timer()
#     list2.append(end - start)
# plot.plot(list1, list2, label="mystery")
# plot.title("Experiment to determine the run time complexity of the mystery function")
# plot.xlabel('number of nodes')
# plot.ylabel('run time')
# plot.legend()
# plot.xticks(np.arange(1, 151, 10))
# plot.show()