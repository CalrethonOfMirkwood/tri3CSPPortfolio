# week 2 factorial

class factorial:
    num = 1
    def __init__(self, n):
        self.num = n
    def calculate(self):
        factorial = 1
        for i in range(1, self.num + 1):
            factorial = factorial * i
        return factorial

# function called by menu.py
def factorialfunction():
    # gives factorial from 1 to 12 by default as example
    for i in range(1,13):
        fact = factorial(i)
        result = fact.calculate()
        print("factorial %d = %d"%(i, result))
        del fact