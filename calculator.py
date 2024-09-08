# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Simple Calculator")
    parser.add_argument("operation", choices=["add", "subtract", "multiply", "divide"], help="Operation to perform")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    result = operations[args.operation](args.a, args.b)
    print(f"Result: {result}")
