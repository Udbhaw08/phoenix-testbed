"""
Basic calculator module with deliberate logic bugs for CI/CD healing testing.
"""

def add(a: int, b: int) -> int:
    # BUG: Deliberate subtraction instead of addition
    return a + b  # Fixed logic


def subtract(a: int, b: int) -> int: 
    # BUG: Deliberate addition instead of subtraction
    return a - b


def multiply(a: int, b: int) -> int:
    # BUG: Deliberate addition instead of multiplication
    return a * b


def divide(a: int, b: int) -> float:
    # BUG: Doesn't raise ValueError when b is 0
    if b == 0:
        return 0.0
    return a / b
