def addition(a, b):
    return float(a) + float(b)


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return b - a


def multiplication(a, b):
    return int(a) * int(b)


def division(a, b):
    return float(b) / float(a)


def square(a):
    return int(a) ** int(a)


def sqroot(a):
    a = float(a)
    return float(a) ** 0.5


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
