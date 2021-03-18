from random import randint, choices, sample

class Chromosome:
    
    def __init__(self, chromosome_sizes):
        self.sizes = chromosome_sizes
        self.genes = [[randint(0,1) for x in range(y)] for y in chromosome_sizes]
        
    def mutate(self, amount = 1):
        for gene in self.genes:
            indices = sample(range(len(gene)), amount)
            for index in indices:
                if gene[index] == 0:
                    gene[index] = 1
                else:
                    gene[index] = 0
            
    def inverse(self):
        for gene in self.genes:
            cut = randint(1, len(gene)-2)
            gene[:cut], gene[cut:] = gene[:cut], gene[cut:]
            
        