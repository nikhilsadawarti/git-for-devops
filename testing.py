"""A simple module demonstrating a greeting function."""


def greet(name):
    """Return a greeting message for the given name.

    Args:
        name (str): The name of the person.

    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}!"


def main():
    """Run the main program."""
    message = greet("Alice")
    print(message)


if __name__ == "__main__":
    main()