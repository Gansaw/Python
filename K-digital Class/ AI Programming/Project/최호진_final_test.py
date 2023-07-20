import numpy as np
import logging


logging.basicConfig(level=logging.INFO)


def measure(func):
    def wrapper(*args, **kwargs):
        calculate = func(*args, **kwargs)        
        logging.info(f"info: {calculate}")
        return calculate
    
    return wrapper


class Evaluator:
    def __init__(self, filename):
        self.filename = filename
        self.equations = self.fileOpen(filename)

    def fileOpen(self, filename):
        f = open(filename, 'rt')
        lines = f.readlines()
        equations = []
        for line in lines:
            equation, x, y = line.strip().split(',')
            equations.append((equation, eval(x), eval(y)))
        return equations
            

    @measure
    def solve(self, idx):
        if idx < 0 or idx >= len(self.equations):
            raise ValueError("Invalid equation idx.")
        equation, x, y = self.equations[idx]
        result = eval(equation, {f"x": x, "y": y})
        print (f"{equation} = {result:.1f}")
        return result


def main():
    evaluator = Evaluator('equations.txt')
    assert np.allclose(evaluator.solve(0), 30)
    assert np.allclose(evaluator.solve(1), -1.9)    


main()
