import itertools

def fibonacci():
    """An infinite generator for Fibonacci numbers."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_squares = (x**2 for x in fibonacci())
first_10_squares = list(itertools.islice(fib_squares, 10))
print(f"The first 10 Fibonacci squares are: {first_10_squares}")  # Output the first 10 Fibonacci squares