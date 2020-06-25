import math


def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a


def multiplication(a, b):
    a = int(a)
    b = int(b)
    return a * b


def division(a, b):
    a = float(a)
    b = float(b)
    return b / a


def square(a):
    int(a)
    return math.pow(a, 2)


def sqroot(a):
    a = float(a)
    return math.sqrt(a)


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
        return round(float(self.result), 9)

    def sqr(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = sqroot(a)
        return round(float(self.result), 8)
