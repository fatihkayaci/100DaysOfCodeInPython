def add(*args):
    print(type(args))
    sum = 0
    for s in args:
        sum += s
    return sum
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

calculate(2, add=3, multiply=5)