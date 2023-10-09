from problem import *
from optimizer import *

def main():
    p, pType = selectProblem()
    alg = selectAlgorithm(pType)    
    alg.run(p)
    p.describe()
    alg.displaySetting()
    p.report()


def selectProblem():
    print("select the problem type: ")
    print(" 1. Numeric")
    print(" 2. Tsp")
    pType = int(input("Enter the number: "))

    if pType == 1:
        p = Numeric()
    elif pType == 2:
        p = Tsp()
    else:
        print("invalid number!")

    p.setVariables()    
    return p, pType

def selectAlgorithm(pType):
    print("select the algorithm: ")
    print(" 1. Steepest Ascent")
    print(" 2. First-Choice")
    print(" 3. Gradient Descent")
    algType = int(input("Enter the algorithm: "))

    optimizers = {1:'SteepestAscent()',2:'FirstChoice()',3:'GradientDescent()'}
    alg = eval(optimizers[algType])    
    alg.setVariables(pType)
    return alg
       

main()