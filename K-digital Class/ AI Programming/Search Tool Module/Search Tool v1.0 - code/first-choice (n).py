import random
import math

LIMIT_STUCK = 100 # Max number of evaluations enduring no improvement
NumEval = 0    # Total number of evaluations
DELTA = 0.01


def main():
    # Create an instance of numerical optimization problem
    p = createProblem()   # 'p': (expr, domain)
    # Call the search algorithm
    solution, minimum = firstChoice(p)
    # Show the problem and algorithm settings
    describeProblem(p)
    displaySetting()
    # Report results
    displayResult(solution, minimum)    


def createProblem(): ###    
    ## Read in an expression and its domain from a file.
    ## Then, return a problem 'p'.
    ## 'p' is a tuple of 'expression' and 'domain'.
    ## 'expression' is a string.
    ## 'domain' is a list of 'varNames', 'low', and 'up'.
    ## 'varNames' is a list of variable names.
    ## 'low' is a list of lower bounds of the varaibles.
    ## 'up' is a list of upper bounds of the varaibles.
    
    fileName = input("Enter the filename of a function: ")    
    infile = open(fileName, 'r')
    expression = infile.readline()
    varNames = []
    low = []
    up = []    
    domain = [varNames, low, up]
    
    for line in infile:
    # 한 줄씩 읽어오기           
        while line != "":
            data = line.split(",")
            varNames.append(data[0])
            low.append(float(data[1]))
            up.append(float(data[2]))
            line = infile.readline()        
    infile.close()
    
    return expression, domain


def firstChoice(p):
    current = randomInit(p)   # 'current' is a list of city ids
    valueC = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK:
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC:
            current = successor
            valueC = valueS
            i = 0              # Reset stuck counter
        else:
            i += 1
    return current, valueC


def randomInit(p): ###
    
    domain = p[1]
    low = domain[1]
    up = domain[2]
    init = []

    for i in range(len(low)):
        r = random.uniform(low[i], up[i])
        init.append(r)
    return init    # Return a random initial point
                   # as a list of values

def evaluate(current, p):
    ## Evaluate the expression of 'p' after assigning
    ## the values of 'current' to the variables
    global NumEval
    
    NumEval += 1
    expr = p[0]         # p[0] is function expression
    varNames = p[1][0]  # p[1] is domain
    for i in range(len(varNames)):
        assignment = varNames[i] + '=' + str(current[i])
        exec(assignment)
    return eval(expr)

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


def mutate(current, i, d, p): ## Mutate i-th of 'current' if legal
    curCopy = current[:]
    domain = p[1]        # [VarNames, low, up]
    l = domain[1][i]     # Lower bound of i-th
    u = domain[2][i]     # Upper bound of i-th
    if l <= (curCopy[i] + d) <= u:
        curCopy[i] += d
    return curCopy

def bestOf(neighbors, p): ###
    best = neighbors[0]
    bestValue = evaluate(best,p)
    for i in range(1,len(neighbors)):
        value = evaluate(neighbors[i],p)
        if value < bestValue:
            best = neighbors[i]
            bestValue = value
        
    return best, bestValue

def describeProblem(p):
    print()
    print("Objective function:")
    print(p[0])   # Expression
    print("Search space:")
    varNames = p[1][0] # p[1] is domain: [VarNames, low, up]
    low = p[1][1]
    up = p[1][2]
    for i in range(len(low)):
        print(" " + varNames[i] + ":", (low[i], up[i])) 

def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)
    print("Max evaluations with no improvement: {0:,} iterations"
          .format(LIMIT_STUCK))

def displayResult(solution, minimum):
    print()
    print("Solution found:")
    print(coordinate(solution))  # Convert list to tuple
    print("Minimum value: {0:,.3f}".format(minimum))
    print()
    print("Total number of evaluations: {0:,}".format(NumEval))

def coordinate(solution):
    c = [round(value, 3) for value in solution]
    return tuple(c)  # Convert the list to a tuple


main()
