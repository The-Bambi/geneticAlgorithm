class GeneticAlgorithm:
    
    def __init__(self, minLimit, maxLimit, valueFunction, epochs):
        self.limits = (minLimit, maxLimit)
        self.valueFunction = valueFunction
        self.epochs = epochs
        self.currEpoch = 0
        self.UI = None