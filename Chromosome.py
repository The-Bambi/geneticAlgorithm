from random import randint, choices, sample

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
    
    
def crossOver(first, second, points = 1):
    offspringA = Chromosome(first.sizes, first.limits, first.precision)
    offspringB = Chromosome(second.sizes, second.limits, second.precision)
    
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
            
class Chromosome:
    
    def __init__(self, chromosome_sizes, limits, precision):
        self.sizes = chromosome_sizes
        self.l = sum(chromosome_sizes)
        self.gene = [randint(0,1) for x in range(self.l)]
        self.limits = limits
        self.precision = precision
        self.values = None
        
    def mutate(self, amount = 1):
        indices = sample(range(self.l), amount)
        for index in indices:
            self.gene[index] = _flip(self.gene[index])
            
    def inverse(self):
        cuts = sample(self.l, k = 2)
        self.gene[cuts[0]:cuts[1]] = [_flip(x) for x in self.gene[cuts[0]:cuts[1]]]
            
    def crossOver(self, other, points = 1):
        offspringA = Chromosome(self.sizes, self.limits, self.precision)
        offspringB = Chromosome(self.sizes, self.limits, self.precision)
        
        offspringA.gene = self.gene
        offspringB.gene = other.gene
        
        if points >= 1:
            indices = sorted(sample(range(self.l), points))
            for i in indices:
                offspringA.gene, offspringB.gene = _mixLists(offspringA.gene, offspringB.gene, i)
        elif point == -1:
            for i in range(0, self.l, 2):
                offspringA.gene[i], offspringB.gene[i] = offspringB.gene[i], offspringA.gene[i]
                
    def calcValues(self):
        vars = []
        i = 0
        for index, size in enumerate(self.sizes):
            low, high = self.limits[index]
            print(int(''.join(map(str, self.gene[i:i+size])), 2))
            vars.append(low + int(''.join(map(str, self.gene[i:i+size])), 2) * (high - low) / (2**size - 1))
            i += size 
        self.values = vars
        return vars