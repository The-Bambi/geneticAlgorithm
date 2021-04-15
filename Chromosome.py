from random import randint, choices, sample
            
class BinaryChromosome:
    
    def __init__(self, chromosome_sizes, limits, precision, function):
        self.sizes = chromosome_sizes
        self.l = sum(chromosome_sizes)
        self.gene = [randint(0,1) for x in range(self.l)]
        self.limits = limits
        self.precision = precision
        self.function = function
        
        self.varValues = self.calcVarValues()
        self.value = self.calcValue()
        
    def __repr__(self):
        return repr(self.value)
        
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
                
    def calcVarValues(self):
        vars = []
        i = 0
        for index, size in enumerate(self.sizes):
            low, high = self.limits[index]
            vars.append(low + int(''.join(map(str, self.gene[i:i+size])), 2) * (high - low) / (2**size - 1))
            i += size 
        return vars
    
    def calcValue(self):
        if self.varValues == None:
            self.varValues = self.calcVarValues()
        varNames = {'x'+str(x):y for x,y in enumerate(self.varValues, 1)}
        return eval(self.function, varNames)