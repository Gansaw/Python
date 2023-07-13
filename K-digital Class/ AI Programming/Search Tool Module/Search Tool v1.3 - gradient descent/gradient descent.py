from problem import Numeric
# tsp 방법을 사용할 수 없다. 수치 데이터에만 사용이 가능하다.


def main():
    p = Numeric()    
    p.setVariables()
    solution, minimum = gradientDescent(p)
    p.storeResult(solution,minimum)
    p.describe()
    displaySetting(p)    
    p.report()

def gradientDescent(p):
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
    return current, valueC


def displaySetting(p):
    print()
    print("Search algorithm: Gradient descent")
    print()
    print("Mutation step size:", p.getDelta())

main()