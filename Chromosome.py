from random import randint, choices, sample

class Chromosome:
    
    def _mixLists(listA, listB, index):
        if len(listA) != len(listB):
            raise Exception("Lists to mix need to be the same length.")
        if index > len(listA):
            raise Exception("Cut index above the list's length.")
        Ahalf = listA[:index]
        halfA = listA[index:]
        
        Bhalf = listB[:index]
        halfB = listB[index:]
        
        return (Ahalf + halfB, Bhalf + halfA)
    
    def _flip(bit):
        if bit = 0:
            return 1
        else:
            return 0
    
    def __init__(self, chromosome_sizes):
        self.sizes = chromosome_sizes
        self.l = sum(chromosome_sizes)
        self.gene = [randint(0,1) for x in range(self.l)]
        
    def mutate(self, amount = 1):
        indices = sample(range(self.l), amount)
        for index in indices:
            self.gene[index] = _flip(self.gene[index])
            
    def inverse(self):
        cuts = sample(self.l, k = 2)
        self.gene[cuts[0]:cuts[1]] = [_flip(x) for x in self.gene[cuts[0]:cuts[1]]]
            
    def crossOver(self, other, points = 1):
        if points >= 1:
            indices = sorted(sample(range(self.l), points))
            for i in indices:
                offspring = _mixLists(gene, other.gene, i)
                gene = offspring[0]
                geneOther = offspring[1]
        elif point == -1:
            for i in range(0, self.l, 2):
                self.gene[i], other.gene[i] = other.gene[i], self.gene[i]
                
    