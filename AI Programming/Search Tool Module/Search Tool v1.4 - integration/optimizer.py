from setup import Setup


class HillClimbing:
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0        
        self._limitStuck = 100 

    def run(self):
        pass       

    def displaySetting(self):        
        if self._pType == 1:
            print()            
            print("Mutation step size:", self._delta)      
        if self._pType == 2:
            print()
            print("Mutation step size:", self._delta)
            print("Max evaluations with no improvement: {0:,} iterations"
          .format(self._limitStuck))
        if self._pType == 3:
            print()
            print("Update rate: ", self._alpha)
            print("Increment for calculating derivatives: ", self._dx)


    def setVariables(self, pType):
        self._pType = pType


class SteepestAscent(HillClimbing):
    def run(self, p):        
        current = p.randomInit()  
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.bestOf(neighbors, p)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)
        
    def bestOf(self, neighbors, p):
        best = neighbors[0]
        bestValue = p.evaluate(best)
        for i in range(1,len(neighbors)):
            value = p.evaluate(neighbors[i])
            if value < bestValue:
                best = neighbors[i]
                bestValue = value
        
        return best, bestValue
    
    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        HillClimbing.displaySetting(self)        

    
class FirstChoice(HillClimbing):
    def run(self, p):
        current = p.randomInit()   # 'current' is a list of city ids
        valueC = p.evaluate(current)
        i = 0
        while i < self._limitStuck:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0              # Reset stuck counter
            else:
                i += 1
        p.storeResult(current, valueC)
    
    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        HillClimbing.displaySetting(self)


class GradientDescent(HillClimbing):    
    def run(self, p):
        current = p.randomInit() 
        valueC = p.evaluate(current)
        while True:
            successor = p.takeStep(current, valueC)
            valueS = p.evaluate(successor)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS

        p.storeResult(current, valueC)
                
    def displaySetting(self):
        print()
        print("Search algorithm: Gradient descent")
        HillClimbing.displaySetting(self)