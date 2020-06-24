def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return float(b) / float(a)


def square(a):
    return a ** a


def sqroot(a):
    return a ** 0.5


class Calculator:
    result = 0

    def __init__(self) -> object:
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def sqr(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = sqroot(a)
        return self.result
