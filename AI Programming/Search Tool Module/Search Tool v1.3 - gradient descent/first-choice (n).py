from problem import Numeric

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement

def main():
    p = Numeric()
    p.setVariables()
    solution, minimum = firstChoice(p)
    # describeProblem(p)    
    p.storeResult(solution, minimum)    
    p.describe()
    displaySetting(p)
    p.report()


def firstChoice(p):
    current = p.randomInit()   # 'current' is a list of city ids
    valueC = p.evaluate(current)
    i = 0
    while i < LIMIT_STUCK:
        successor = p.randomMutant(current)
        valueS = p.evaluate(successor)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC

def displaySetting(p):
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", p.getDelta())
    print("Max evaluations with no improvement: {0:,} iterations"
          .format(LIMIT_STUCK))

main()