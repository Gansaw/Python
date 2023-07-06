from numeric import *


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = steepestAscent(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)    


def steepestAscent(p):
    current = randomInit(p) # 'current' is a list of values
    valueC = evaluate(current, p)
    while True:
        neighbors = mutants(current, p)
        successor, valueS = bestOf(neighbors, p)
        if valueS >= valueC:
            break
        else:
            current = successor
            valueC = valueS
    return current, valueC


def randomMutant(current, p):
    i = random.randint(0,len(current)-1)
    if random.uniform(0, 1)>0.5:
        d = DELTA
    else:
        d = -DELTA
    
    return mutate(current, i, d, p)

def mutants(current, p): ###
    neighbors = []
    
    for i in range(len(current)):
        mutant = mutate(current, i, DELTA, p)        
        neighbors.append(mutant)        
        mutant = mutate(current, i, -DELTA, p)
        neighbors.append(mutant)        
    
    for j in range(len(current)): 
        for k in range(j+1, len(current)):
            mutant = mutate(current, j, DELTA, p)
            neighbors.append(mutant)
            mutant = mutate(current, j, -DELTA, p)
            neighbors.append(mutant)
            mutant = mutate(mutant, k, DELTA, p)
            neighbors.append(mutant)
            mutant = mutate(mutant, i, -DELTA, p)
            neighbors.append(mutant)
    return neighbors     # Return a set of successors

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)

main()