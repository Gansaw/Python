from Problem import Tsp 

def main():
    p = Tsp()    
    solution, minimum = firstChoice(p)
    describeProblem(p)
    displaySetting()
    displayResult(solution, minimum)

def firstChoice(p):
    current = randomInit(p) 
    valueC = evaluate(current, p)
    i = 0
    while i < LIMIT_STUCK: 
        successor = randomMutant(current, p)
        valueS = evaluate(successor, p)
        if valueS < valueC: 
            current = successor
            valueC = valueS
            i = 0           
        else:
            i += 1
    return current, valueC

def randomMutant(current, p): 
    i = random.randint(0, len(current)-1) 
    if random.uniform(0,1)>0.5: 
        d = DELTA
    else:
        d = -DELTA    

    return mutate(current, i, d, p)


def displaySetting():
    print()
    print("Search algorithm: First-Choice Hill Climbing")
    print()
    print("Mutation step size:", DELTA)
main()