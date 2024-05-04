# 1. Positional Arguments:
# They are passed to a function based on their position in the function's definition.
# The order and number of positional arguments must match the function's parameter list.

def greet(name, message):
    print(f"Hello, {name}! {message}")

greet("Alice", "How are you?")


# 2. Keyword Arguments:
# These arguments are identified by their parameter name.
# They allow you to specify arguments in any order.

def greet(name, message):
    print(f"Hello, {name}! {message}")

greet(message="How are you?", name="Bob")


# 3. Default Arguments:
# These are parameters that have default values specified in the function definition.
# If the caller does not provide a value for these arguments, the default value is used.

def greet(name, message="Good morning!"):
    print(f"Hello, {name}! {message}")

greet("Alice")


# 4. Variable-Length Arguments:
# These allow you to pass a variable number of arguments to a function.
# There are two types:
#  -> *Arbitrary Argument Lists (args): Allows a function to accept an arbitrary number of positional arguments.
#  -> **Arbitrary Keyword Argument Dictionaries (kwargs): Allows a function to accept an arbitrary number of keyword arguments.

def sum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum(1, 2, 3, 4, 5))
