from abc import ABC, abstractmethod

class Graph(ABC):
    
    @abstractmethod 
    def get_adj_nodes(self, node):
        pass

    @abstractmethod 
    def add_node(self, node):
        pass

    @abstractmethod 
    def add_edge(self, start, end, w):
        pass

    @abstractmethod 
    def get_num_of_nodes(self):
        pass

    @abstractmethod 
    def w(self, node):
        pass