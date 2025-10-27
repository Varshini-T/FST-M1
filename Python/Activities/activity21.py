import pytest

# --- Calculator functions ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_sum_of_two_numbers():
    assert add(10, 5) == 15

def test_difference_of_two_numbers():
    assert subtract(10, 5) == 5
