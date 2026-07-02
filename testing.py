"""Simple calculator module."""


def add(number1, number2):
    """Return the sum of two numbers."""
    return number1 + number2


def subtract(number1, number2):
    """Return the difference between two numbers."""
    return number1 - number2


def multiply(number1, number2):
    """Return the product of two numbers."""
    return number1 * number2


def divide(number1, number2):
    """Return the quotient of two numbers.

    Raises:
        ValueError: If the second number is zero.
    """
    if number2 == 0:
        raise ValueError("Cannot divide by zero.")
    return number1 / number2


def main():
    """Run the calculator example."""
    first_number = 10
    second_number = 5

    print(f"Addition: {add(first_number, second_number)}")
    print(f"Subtraction: {subtract(first_number, second_number)}")
    print(f"Multiplication: {multiply(first_number, second_number)}")
    print(f"Division: {divide(first_number, second_number)}")


if __name__ == "__main__":
    main()