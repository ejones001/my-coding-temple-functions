
# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y


# Get user input for numbers and operation choice
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

# Perform chosen operation
if operation == '+':
    print("Result:", add(num1, num2))
elif operation == '-':
    print("Result:", subtract(num1, num2))
elif operation == '*':
    print("Result:", multiply(num1, num2))
elif operation == '/':
    print("Result:", divide(num1, num2))
else:
    print("Invalid operation!")
