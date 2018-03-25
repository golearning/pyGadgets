# Some statistics functions

def sqrt(x):
    return pow(x, 0.5)

def avg(l):
    try:
        return sum(l) / len(l)
    except ZeroDivisionError:
        raise ValueError("The list cannot be empty")

def stddev(l, a=None, unbiased=0):
    if a is None:
        a = avg(l)
    return sqrt(sum([(i-a)**2 for i in l]) / (len(l) - unbiased))

def ubstddev(l, a=None):
    return stddev(l, a=a, unbiased=1)

def bstddev(l, a=None):
    return stddev(l, a=a, unbiased=0)

class linreg:
    @staticmethod
    def b(x, y):
        n, ax, ay = len(x), avg(x), avg(y)
        return (sum([a * b for a, b in zip(x, y)]) - n * ax * ay) / (sum([i**2 for i in x]) - n * ax**2)

    @staticmethod
    def a(x, y):
        return avg(y) - b(x, y) * avg(x)

    @staticmethod
    def re(x, y):
        n, ax, ay = len(x), avg(x), avg(y)
        return (sum([a * b for a, b in zip(x, y)]) - n * ax * ay) / pow((sum([i**2 for i in x]) - n * ax**2)*(sum([i**2 for i in y]) - n * ay**2), 0.5)