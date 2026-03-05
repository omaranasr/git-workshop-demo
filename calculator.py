# calculator.py - Simple calculator for Git workshop

def add(a, b):
   """Return the sum of a and b with logging."""
   result = a + b
   print(f"LOG: add({a}, {b}) = {result}")
   return result

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b



if __name__ == "__main__":
    print("Addition:    ", add(10, 5))
    print("Subtraction: ", subtract(10, 5))
    print("Multiply:    ", multiply(10, 5))
    print("Division:    ", divide(10, 5))