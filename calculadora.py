import sys


class Calculadora:

    def __init__(self):
        self.value = 0

    def add(self, a, b):
        self.value = a + b

    def substract(self, a, b):
        self.value = a - b

    def div(self, a, b):
        self.value = a / b

    def multiply(self, a, b):
        self.value = a * b

    def __square(self, n, i, j):
        mid = (i + j) / 2
        mul = mid * mid

        if mul == n or abs(mul - n) < 0.00001:
            return mid
        elif mul < n:
            return self.__square(n, mid, j)
        else:
            return self.__square(n, i, mid)

    def sqrt(self, n):
        i = 1
        res = 0
        found = False
        while not found:
            if i * i == n:
                found = True
            elif i * i > n:
                res = self.__square(n, i - 1, i)
                found = True
            i += 1

        if res == 0:
            self.value = i - 1
        else:
            self.value = res


if __name__ == "__main__":
    c = Calculadora()
    switcher = {
        "add": lambda: c.add(int(sys.argv[2]), int(sys.argv[3])),
        "substract": lambda: c.substract(int(sys.argv[2]), int(sys.argv[3])),
        "div": lambda: c.div(int(sys.argv[2]), int(sys.argv[3])),
        "multiply": lambda: c.multiply(int(sys.argv[2]), int(sys.argv[3])),
        "sqrt": lambda: c.sqrt(float(sys.argv[2]))
    }

    func = switcher.get(sys.argv[1])
    func()
    print(c.value)
