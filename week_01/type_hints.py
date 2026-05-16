from typing import Optional, Union, Callable
import time


# Optional - a value that could be None
def find_user(user_id: int) -> Optional[str]:
    """Return username if found, None if not."""
    users = {1: "diego", 2: "alice", 3: "bob"}
    return users.get(user_id)


# Union - a value that could be one of several types
def process_input(data: Union[int, float, str]) -> float:
    """Convert any numeric input to float."""
    return float(data)


# Callable - a function passed as argument
def apply_twice(func: Callable[[float], float], value: float) -> float:
    """Apply a function to a value twice."""
    return func(func(value))


def double(x: float) -> float:
    return x * 2


if __name__ == "__main__":
    # Optional
    print(find_user(1))   # diego
    print(find_user(99))  # None

    # Union
    print(process_input(42))     # 42.0
    print(process_input("3.14")) # 3.14

    # Callable
    print(apply_twice(double, 3.0))  # 12.0