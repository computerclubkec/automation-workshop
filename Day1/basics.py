# 1. Introduction to Python
# Brief overview of Python's capabilities and applications in automation.

# 2. Basic Syntax and Data Types 
# Variables and Data Types: integers, floats, strings, and booleans.
# Basic Operations: arithmetic operations, string concatenation.


# Variables and Data Types
integer_var = 10
float_var = 20.5
string_var = "Hello, World!"
boolean_var = True

# Basic Operations
sum_result = integer_var + float_var
concat_result = string_var + " This is Python."
boolean_check = integer_var > float_var

print(sum_result)  # 30.5
print(concat_result)  # Hello, World! This is Python.
print(boolean_check)  # False


# 3. Control Structures (20 minutes)
# Conditional Statements: if, elif, else.
# Loops: for loop, while loop.

# Conditional Statements
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Loops
# For loop
for i in range(5):
    print(i)  # Prints 0 to 4

# While loop
count = 0
while count < 5:
    print(count)
    count += 1  # Prints 0 to 4
# 4. Functions (15 minutes)
# Defining Functions: def keyword, parameters, return statement.
# Calling Functions.


# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Calling a function
message = greet("Alice")
print(message)  # Hello, Alice!
# 5. Lists and Dictionaries (20 minutes)
# Lists: creation, indexing, methods (append, remove).
# Dictionaries: creation, accessing values, methods (keys, values).

# Lists
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
print(fruits)  # ['apple', 'banana', 'cherry', 'date']
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'date']

# Dictionaries
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person["name"])  # John
person["email"] = "john@example.com"
print(person)  # {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}
# 6. Basic File Handling (15 minutes)
# Reading from a file.
# Writing to a file.


# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a test file.")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # Hello, this is a test file.
