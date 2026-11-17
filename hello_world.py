# My first ile tracked by Git
#Author: Andrea Tepes

def greet(name):
    """Return a welcome message for the given name."""
    return f"Hello, {name}! Welcome to Git."

#This bloc runs only when the file is executed directly,
## not when it is imported as a module from another file.
if __name__ == "__main__":
    print(greet("World")) #Call the greet function and print the result
    print(farewell("World")) #Call the farewell function and print the result
    