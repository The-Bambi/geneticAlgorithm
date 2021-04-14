import math

class GeneticAlgorithm:
    
    def __init__(self, limits, precision, valueFunction, epochs):
        self.limits = limits
        self.valueFunction = valueFunction
        self.epochs = epochs
        self.currEpoch = 0
        self.UI = None