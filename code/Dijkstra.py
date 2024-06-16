import min_heap

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