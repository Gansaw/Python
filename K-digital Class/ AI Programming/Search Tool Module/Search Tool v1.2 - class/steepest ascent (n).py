from problem import Numeric


def main():
    p = Numeric()    
    p.setVariables()
    solution, minimum = steepestAscent(p)
    p.describe()
    displaySetting(p)
    p.storeResult(solution,minimum)
    p.report()

def steepestAscent(p):
    current = p.randomInit() 
    valueC = p.evaluate(current)
    while True:
        neighbors = p.mutants(current)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC

def bestOf(neighbors, p):
    best = neighbors[0]
    bestValue = p.evaluate(best)
    for i in range(1,len(neighbors)):
        value = p.evaluate(neighbors[i])
        if value < bestValue:
            best = neighbors[i]
            bestValue = value
        
    return best, bestValue

def displaySetting(p):
    print()
    print("Search algorithm: Steepest-Ascent Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())

main()