# Regular loop - the way you probably write it now
squares_loop: list[int] = []
for n in range(10):
    squares_loop.append(n ** 2)

# List comprehension - the pythonic way
squares: list[int] = [n ** 2 for n in range(10)]

# With filter
even_squares: list[int] = [n ** 2 for n in range(10) if n % 2 == 0]

print(squares)
print(even_squares)

squares_list: list[int] = [n ** 2 for n in range(1_000_000)]

squares_gen = (n ** 2 for n in range(1_000_000))

print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
print(next(squares_gen))  # 4

def batch_data(data: list[float], batch_size: int):
    """Yield data in chunks without loading everything into memory."""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

dataset: list[float] = list(range(100))
for batch in batch_data(dataset, batch_size=10):
    print(f"Batch: {batch[:3]}...")

import time
from functools import wraps


def timer(func):
    """Measure how long a function takes to run."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


@timer
def slow_sum(n: int) -> int:
    """Sum numbers the slow way."""
    total = 0
    for i in range(n):
        total += i
    return total


@timer
def fast_sum(n: int) -> int:
    """Sum numbers the fast way."""
    return sum(range(n))


slow_sum(1_000_000)
fast_sum(1_000_000)