import csv
import itertools
from math import radians, sin, cos, sqrt, atan2
import DirectedWeightedGraph
import Dijkstra
import A_star
import timeit
import matplotlib.pyplot as plot

"""
Experiment 2

Compare runtime of shortest path algorithms Dijkstra to A* with an efficient and inefficient heuristic function.
Use data on London's subway systems to test.
"""


# heuristic function and setup -----------------------------

# extract information from csv and save in a dictionary
# used to make heuristic efficient
class StationInfo:
    def __init__(self):
        self.stations = {}
        with open("code/csv_files/london_stations.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                station = {
                    'latitude': float(row[1]),
                    'longitude': float(row[2]),
                    'name': row[3],
                    'display_name': row[4],
                    'zone': float(row[5]),
                    'total_lines': int(row[6]),
                    'rail': bool(row[7])
                }
                self.stations[int(row[0])] = station

    def get_station_info(self, station_id):
        return self.stations.get(station_id)

stationinfo = StationInfo()

# used as heuristic
def distance_between_stations(station1, station2):
    station1 = stationinfo.get_station_info(station1)
    station2 = stationinfo.get_station_info(station2)

    # use below definitions instead to make heuristic inefficient
    #station1 = get_station_info(station1)
    #station2 = get_station_info(station2)

    # radius of earth in km
    R = 6373.0

    # convert latitudes and longitudes to radians
    lat1 = radians(station1.get("latitude"))
    lon1 = radians(station1.get("longitude"))
    lat2 = radians(station2.get("latitude"))
    lon2 = radians(station2.get("longitude"))

    # difference between latitudes and longitudes
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # use some cursed formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c



# set up graph --------------------------------------

def add_stations_to_graph(graph):
    with open('code/csv_files/london_stations.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (row[0] != "id"):
                graph.add_node(int(row[0]))

def add_stations_connections_to_graph(graph):
    with open('code/csv_files/london_connections.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if (row[0] != 'station1'):
                station1 = get_station_info(row[0])
                station2 = get_station_info(row[1])
                distance = distance_between_stations(station1.get('id'), station2.get('id'))
                graph.add_edge(station1.get('id'), station2.get('id'), distance)
                graph.add_edge(station2.get('id'), station1.get('id'), distance)



# gets information from csv -----------------------------------------

# returns station ids
def get_all_stations():
    with open('code/csv_files/london_stations.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        stations = []
        for row in reader:
            if (row[0] != "id"):
                if (row[0] not in stations):
                    stations.append(int(row[0]))
    return stations

# returns station info
def get_station_info(id):
    with open('code/csv_files/london_stations.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == str(id):
                return {
                    'id': int(row[0]),
                    'latitude': float(row[1]),
                    'longitude': float(row[2]),
                    'name': row[3],
                    'display_name': row[4],
                    'zone': float(row[5]),
                    'total_lines': int(row[6]),
                    'rail': int(row[7])
                }
    return None

# return station connections
def get_station_info_connections(id):
    with open('code/csv_files/london_connections.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == str(id):
                return {
                    'id': int(row[0]),
                    'line': int(row[2])
                }
    return None



# get specific pairs ---------------------------

def get_all_stations_same_line(station_pairs):
    pairs = []
    for pair in station_pairs:
        if (get_station_info_connections(pair[0]) is not None and get_station_info_connections(pair[1]) is not None):
            if (get_station_info_connections(pair[0]).get("line") == get_station_info_connections(pair[1]).get("line")):
                pairs.append(pair)
    return pairs

def get_all_stations_adjacent_line(station_pairs):
    pairs = []
    for pair in station_pairs:
        if (get_station_info_connections(pair[0]) is not None and get_station_info_connections(pair[1]) is not None):
            if (get_station_info_connections(pair[0]).get("line") == get_station_info_connections(pair[1]).get("line") + 1):
                pairs.append(pair)
    return pairs

def get_all_stations_multiple_line(station_pairs):
    pairs = []
    for pair in station_pairs:
        if (get_station_info_connections(pair[0]) is not None and get_station_info_connections(pair[1]) is not None):
            if (get_station_info_connections(pair[0]).get("line") != get_station_info_connections(pair[1]).get("line")
                and get_station_info_connections(pair[0]).get("line") != get_station_info_connections(pair[1]).get("line") + 1):
                pairs.append(pair)
    return pairs



# Helper function(s) ----------------------------

# returns possible pairs from an array
def station_pairs(stations):
    return list(itertools.combinations(stations, 2))



# experiment ------------------------------------

def experiment():
    # setup graph
    x = DirectedWeightedGraph.DirectedWeightedGraph(500)
    add_stations_to_graph(x)
    add_stations_connections_to_graph(x)

    # setup times
    a_star_times = []
    dijkstra_times = []
    
    r = 0 # to skip some experiments if needed

    # setup order of pairs
    stationsOrdered = get_all_stations_same_line(station_pairs(get_all_stations())) # pairs on the same line
    stationsOrdered = stationsOrdered + get_all_stations_adjacent_line(station_pairs(get_all_stations())) # pairs on adjacent lines
    stationsOrdered = stationsOrdered + get_all_stations_multiple_line(station_pairs(get_all_stations())) # pairs that require multiple transfers

    for s in station_pairs(get_all_stations()):
        r = r + 1
        
        if (r % 1000 == 0): # to skip some experiments if needed
            start1 = timeit.default_timer()
            A_star.a_star(x, s[0], s[1], distance_between_stations)
            end1 = timeit.default_timer()
            a_star_times.append(end1 - start1)

            start2 = timeit.default_timer()
            Dijkstra.dijkstra(x, s[0])[s[1]]
            end2 = timeit.default_timer()
            dijkstra_times.append(end2 - start2)

    results = []
    results.append(a_star_times)
    results.append(dijkstra_times)
    return results


times = experiment()
plot.plot(times[0], label = "A*")
plot.plot(times[1], label = "Dijkstra")
plot.xlabel('Number of Experiments') 
plot.ylabel('Time Taken')
plot.title("A* vs Dijkstra on All Pairs of Stations")
plot.legend()
plot.show()
