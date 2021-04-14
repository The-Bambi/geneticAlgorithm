from Chromosome import *
import math

class Population:
    
    def __init__(self, abundance, limits, precision, function):
        self.sizes = [round(math.log2((y - x) * 10**precision)+1) for x,y in limits]
        self.current = [Chromosome(self.sizes, limits, precision) for i in range(abundance)]
        self.offsprings = []
        self.elites = []
        
    def evolve(self):
        pass
    
    