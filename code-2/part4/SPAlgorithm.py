from abc import ABC, abstractmethod

class SPAlgorithm(ABC):
    
    @abstractmethod 
    def calc_sp(graph, source, dest):
        pass