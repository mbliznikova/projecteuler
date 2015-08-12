import itertools
def fibonacci():
    a = 1
    b = 2
    yield a
    while True:
        yield b
        a, b = b, a + b

g = fibonacci()
print list(itertools.islice(g, 10))
