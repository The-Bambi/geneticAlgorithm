from Chromosome import *

class Population:
    
    def __init__(self, size, chromosome_sizes):
        self.current = [Chromosome(chromosome_sizes) for x in range(size)]
        self.offsprings = []
        
        
        