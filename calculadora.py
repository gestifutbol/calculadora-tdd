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

