class factorial:
    num = 1
    def __init__(self, n):
        self.num = n
    def calculate(self):
        factorial = 1
        for i in range(1, self.num + 1):
            factorial = factorial * i
        return factorial

def factorialfunction():
    for i in range(1,13):
        fact = factorial(i)
        result = fact.calculate()
        print("factorial %d = %d"%(i, result))
        del fact