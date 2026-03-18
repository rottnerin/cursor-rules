ABOUTME: Demonstrates a simple greeting for the cursor rules repository.
ABOUTME: Provides a reusable function for friendly console output.

def greet(name: str) -> str:
    """Return a friendly greeting for the provided name."""
    return f"Hello, {name}! Keep experimenting with Cursor."


if __name__ == "__main__":
    print(greet("Cursor Friend"))
