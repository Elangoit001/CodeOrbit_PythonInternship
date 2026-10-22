"""Task 1: Simple Calculator
Performs basic arithmetic operations with input validation.
"""

# ---- Arithmetic functions ----
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Raises ZeroDivisionError if b is 0 (handled in main loop)
    return a / b


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


def main():
    print("=== Simple Calculator ===")
    while True:
        # Show menu
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please pick 1-5.")
            continue

        # Take user input
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        # Perform the operation and handle errors
        try:
            if choice == "1":
                print(f"Result: {a} + {b} = {add(a, b)}")
            elif choice == "2":
                print(f"Result: {a} - {b} = {subtract(a, b)}")
            elif choice == "3":
                print(f"Result: {a} * {b} = {multiply(a, b)}")
            else:
                print(f"Result: {a} / {b} = {divide(a, b)}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero!")


if __name__ == "__main__":
    main()