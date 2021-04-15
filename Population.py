from Chromosome import *
import math
from random import random, shuffle

def crossOver(first, second, points = 1):
    offspringA = BinaryChromosome(first.sizes, first.limits, first.precision, first.function)
    offspringB = BinaryChromosome(second.sizes, second.limits, second.precision, first.function)
    
    offspringA.gene = first.gene
    offspringB.gene = second.gene
    
    if points >= 1:
        indices = sorted(sample(range(first.l), points))
        for i in indices:
            offspringA.gene, offspringB.gene = _mixLists(offspringA.gene, offspringB.gene, i)
    elif point == -1:
        for i in range(0, first.l, 2):
            offspringA.gene[i], offspringB.gene[i] = offspringB.gene[i], offspringA.gene[i]
    
    return (offspringA, offspringB)

def _mixLists(listA, listB, index):
    if len(listA) != len(listB):
        raise Exception("Lists to mix need to be the same length.")
    if index > len(listA):
        raise Exception("Cut index is above the list's length.")
    Ahalf = listA[:index]
    halfA = listA[index:]
    
    Bhalf = listB[:index]
    halfB = listB[index:]
    
    return (Ahalf + halfB, Bhalf + halfA)


def _flip(bit):
    if bit == 0:
        return 1
    else:
        return 0
    
def sortList(alist):
    alist.sort(key = lambda chromosome: chromosome.calcValue())
    return alist
class Population:
    
    def __init__(self, abundance, limits, precision, function, elitesNumber = 0):
        self.sizes = [round(math.log2((y - x) * 10**precision)+1) for x,y in limits]
        self.currentGeneration = sortList([BinaryChromosome(self.sizes, limits, precision, function) for i in range(abundance)])
        self.goalFunction = function
        self.limits = limits
        
        self.offspringGeneration = []
        self.elites = set()
        
    def randomCross(self, probability = 0.25, crossPoints = 1):
        toBeCrossed = []
        for index in range(len(self.currentGeneration)):
            if random() < probability:
                toBeCrossed.append(self.currentGeneration[index])
                
            else:
                self.offspringGeneration.append(self.currentGeneration[index])
        
        shuffle(toBeCrossed)
        print("{} chromosomes were chosen to cross over randomly.".format(len(toBeCrossed)))
        if len(toBeCrossed)%2 != 0:
            self.offspringGeneration.append(toBeCrossed.pop())
            print("Popping 1")
        
        for index in range(0, len(toBeCrossed), 2):
            newPair = crossOver(toBeCrossed[index], toBeCrossed[index+1], crossPoints)
            self.offspringGeneration.append(newPair[0])
            self.offspringGeneration.append(newPair[1])
        
        return self.offspringGeneration
        
    def mutate(self, p = 0.01):
        for i in range(len(self.offspringGeneration)):
            for g in range(len(self.offspringGeneration[i].gene)):
                if random() < p:
                    b = self.offspringGeneration[i].gene[g]
                    self.offspringGeneration[i].gene[g] = _flip(b)

    def safeElites(self, n):
        for i in range(n):
            elite = self.currentGeneration.pop(0)
            print(elite)
            self.offspringGeneration.append(elite)
    
    def evolve(self):
        self.safeElites(2)
        self.randomCross()
        self.mutate()
        self.currentGeneration = sortList(self.offspringGeneration)
        self.offspringGeneration = []
        
            
    