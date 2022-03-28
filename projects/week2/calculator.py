import random
import math

class calculator:
    a = 0
    b = 0
    def __init__(self, inputa):
        self.a = inputa
    def __init__(self, inputa, inputb):
        self.a = inputa
        self.b = inputb
    def add(self):
        return self.a+self.b
    def subtract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b
    def divide(self):
        if(self.b==0):
            print("Cannot divide by 0. Returning 0")
            return 0
        return self.a/self.b
    def squareroot(self):
        return math.sqrt(self.a)

def calcfunction():
    for i in range(5):
        a = random.randint(0, 100)
        b = random.randint(0, 10)
        calc = calculator(a,b)
        print("%d+%d = %d"%(a, b, calc.add()))
        print("%d-%d = %d"%(a, b, calc.subtract()))
        print("%d*%d = %d"%(a, b, calc.multiply()))
        print("%d/%d = %f"%(a, b, calc.divide()))
        print("Squareroot(%d) = %f"%(a, calc.squareroot()))
        del calc