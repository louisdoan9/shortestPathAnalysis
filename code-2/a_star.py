'''
Part 3: A* algorithm
'''

import min_heap

def a_star(G, s, d, h):
    pred = {}
    dist = {}
    path = []
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(s, h(s, d))

    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        if current_node == d:
            break
        dist[current_node] = current_element.key - h(current_node, d)
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour) + h(neighbour, d))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node

    # Create the shortest path
    path = [d]
    while path[-1] != s:
        path.append(pred[path[-1]])
    path.reverse()

    return path
    #return dist[d]